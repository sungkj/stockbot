import yaml
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from utils.logger import setup_logger
from tasks.kiwoom_api import KiwoomApiTask

logger = setup_logger(__name__)

class TeleBotApp:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
            
        bot_token = self.config["telegram"]["bot_token"]
        self.application = Application.builder().token(bot_token).build()
        self.kiwoom_task = KiwoomApiTask()
        self._register_handlers()

    def _register_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start_command))
        # 텔레그램 공식 명령어는 영문만 지원하므로, 한글 명령어는 정규식을 이용해 처리합니다.
        self.application.add_handler(MessageHandler(filters.Regex(r"^/잔고"), self.balance_command))
        
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

    async def start(self):
        logger.info("Initializing python-telegram-bot...")
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()
        
        stop_event = asyncio.Event()
        await stop_event.wait()