from utils.logger import setup_logger
from utils.config_manager import ConfigManager

logger = setup_logger(__name__)

class TelegramMonitor:
    """타 텔레그램 방 모니터링 (User-Bot)"""
    def __init__(self, config_path="config.yaml"):
        self.name = "타 텔레그램 방 모니터링"
        self.config_manager = ConfigManager(config_path)
        # TODO: Pyrogram 또는 Telethon 클라이언트 초기화
        
    async def start(self):
        logger.info(f"Starting User-Bot for {self.name}")
        stocks = self.config_manager.get_stocks()
        logger.debug(f"텔레그램 방 모니터링 대상 종목: {list(stocks.keys())}")
        
        # TODO: User-bot 실행 및 이벤트 핸들러(특정 방 키워드 감지) 부착
        # 타 텔레그램 방에서 종목 및 하위 키워드와 매칭되는 메시지를 필터링하도록 로직 추가 예정