import asyncio
from utils.logger import setup_logger

logger = setup_logger(__name__)

class GoogleTrendsTask:
    def __init__(self):
        self.name = "구글 트렌드 분석"

    async def run(self):
        logger.info(f"실행 중: {self.name}")
        # TODO: pytrends 수집 및 utils.chart_drawer를 이용한 이미지 생성 로직 구현
        await asyncio.sleep(1)
        
        return "[구글 트렌드] 오늘의 트렌드 리포트입니다. (Mock)", None