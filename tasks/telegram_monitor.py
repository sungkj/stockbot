from utils.logger import setup_logger

logger = setup_logger(__name__)

class TelegramMonitor:
    """타 텔레그램 방 모니터링 (User-Bot)"""
    def __init__(self):
        self.name = "타 텔레그램 방 모니터링"
        # TODO: Pyrogram 또는 Telethon 클라이언트 초기화
        
    async def start(self):
        logger.info(f"Starting User-Bot for {self.name}")
        # TODO: User-bot 실행 및 이벤트 핸들러(특정 방 키워드 감지) 부착