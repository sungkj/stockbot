import yaml
import asyncio
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from utils.logger import setup_logger
from utils.config_manager import ConfigManager
from tasks.kiwoom_api import KiwoomApiTask

logger = setup_logger(__name__)

class TeleBotApp:
    def __init__(self, config_path="config.yaml"):
        self.config_manager = ConfigManager(config_path)
        self.config = self.config_manager.load()
            
        bot_token = self.config["telegram"]["bot_token"]
        self.application = Application.builder().token(bot_token).build()
        self.kiwoom_task = KiwoomApiTask()
        self._register_handlers()

    def _register_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start_command))
        # 텔레그램 공식 명령어는 영문만 지원하므로, 한글 명령어는 정규식을 이용해 처리합니다.
        self.application.add_handler(MessageHandler(filters.Regex(r"^/잔고"), self.balance_command))
        self.application.add_handler(MessageHandler(filters.Regex(r"^/종목등록"), self.add_stock_command))
        self.application.add_handler(MessageHandler(filters.Regex(r"^/키워드등록"), self.add_keyword_command))
        self.application.add_handler(MessageHandler(filters.Regex(r"^/종목조회"), self.list_stocks_command))
        
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("텔레봇이 시작되었습니다! 모니터링 및 스케줄링이 동작합니다.")

    async def balance_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("⏳ 키움증권 계좌 정보를 조회 중입니다. 잠시만 기다려주세요...")
        try:
            message, _ = await self.kiwoom_task.run()
            await update.message.reply_text(message, parse_mode="Markdown")
        except Exception as e:
            logger.error(f"잔고 조회 중 오류 발생: {e}")
            await update.message.reply_text("⚠️ 잔고 조회 중 오류가 발생했습니다.")

    async def add_stock_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
        match = re.match(r"^/종목등록\s+(.+)$", text)
        if not match:
            await update.message.reply_text("⚠️ 사용법: /종목등록 <종목명>\n예) /종목등록 카카오")
            return
        
        stock_name = match.group(1).strip()
        if self.config_manager.add_stock(stock_name):
            await update.message.reply_text(f"✅ '{stock_name}' 종목이 성공적으로 등록되었습니다.")
        else:
            await update.message.reply_text(f"⚠️ '{stock_name}' 종목은 이미 등록되어 있습니다.")

    async def add_keyword_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
        match = re.match(r"^/키워드등록\s+(.+?)\s+(.+)$", text)
        if not match:
            await update.message.reply_text("⚠️ 사용법: /키워드등록 <종목명> <키워드>\n예) /키워드등록 카카오 인공지능")
            return
            
        stock_name = match.group(1).strip()
        keyword = match.group(2).strip()
        
        # 종목이 없으면 자동 등록(또는 에러 처리할 수 있으나 여기서는 등록해줌)
        if self.config_manager.add_keyword(stock_name, keyword):
            await update.message.reply_text(f"✅ '{stock_name}' 종목에 '{keyword}' 키워드가 등록되었습니다.")
        else:
            await update.message.reply_text(f"⚠️ '{stock_name}' 종목에 '{keyword}' 키워드가 이미 존재합니다.")

    async def list_stocks_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        stocks = self.config_manager.get_stocks()
        if not stocks:
            await update.message.reply_text("ℹ️ 등록된 종목이 없습니다.")
            return
            
        message = "📊 *현재 등록된 종목 및 키워드*\n\n"
        for stock, keywords in stocks.items():
            keyword_str = ", ".join(keywords) if keywords else "키워드 없음"
            message += f"- *{stock}*: {keyword_str}\n"
            
        await update.message.reply_text(message, parse_mode="Markdown")

    async def start(self):
        logger.info("Initializing python-telegram-bot...")
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()
        
        stop_event = asyncio.Event()
        await stop_event.wait()