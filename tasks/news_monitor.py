import asyncio
from utils.logger import setup_logger
from utils.config_manager import ConfigManager

logger = setup_logger(__name__)

class NewsMonitor:
    def __init__(self, config_path="config.yaml"):
        self.name = "실시간 뉴스 모니터링"
        self.config_manager = ConfigManager(config_path)

    async def run(self):
        logger.info(f"실행 중: {self.name}")
        stocks = self.config_manager.get_stocks()
        logger.debug(f"현재 등록된 종목 및 키워드: {stocks}")
        
        # TODO: RSS나 크롤링 로직 구현 (기존 데이터와 비교하여 신규 기사만 필터링)
        # 종목별 키워드를 기반으로 뉴스 필터링 로직 추가 예정
        await asyncio.sleep(1) 
        
        return "[뉴스 모니터링] 신규 기사가 없습니다. (Mock)", None