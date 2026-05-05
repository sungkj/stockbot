import yaml
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from utils.logger import setup_logger

logger = setup_logger(__name__)

class TeleBotApp:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
            
        bot_token = self.config["telegram"]["bot_token"]
        self.application = Application.builder().token(bot_token).build()
        self._register_handlers()

    def _register_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start_command))
        
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("텔레봇이 시작되었습니다! 모니터링 및 스케줄링이 동작합니다.")

    async def start(self):
        logger.info("Initializing python-telegram-bot...")
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()
        
        stop_event = asyncio.Event()
        await stop_event.wait()