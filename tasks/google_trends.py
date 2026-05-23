import asyncio
from utils.logger import setup_logger
from utils.config_manager import ConfigManager

logger = setup_logger(__name__)

class GoogleTrendsTask:
    def __init__(self, config_path="config.yaml"):
        self.name = "구글 트렌드 분석"
        self.config_manager = ConfigManager(config_path)

    async def run(self):
        logger.info(f"실행 중: {self.name}")
        stocks = self.config_manager.get_stocks()
        logger.debug(f"트렌드 분석 대상 종목: {list(stocks.keys())}")
        
        # TODO: pytrends 수집 및 utils.chart_drawer를 이용한 이미지 생성 로직 구현
        # 종목별 키워드를 기반으로 트렌드 데이터를 수집하도록 로직 추가 예정
        await asyncio.sleep(1)
        
        return "[구글 트렌드] 오늘의 트렌드 리포트입니다. (Mock)", None