from utils.logger import setup_logger

logger = setup_logger(__name__)

class KiwoomApiTask:
    def __init__(self):
        self.name = "키움증권 API 연동"
        
    async def run(self):
        logger.info(f"실행 중: {self.name}")
        # TODO: 키움증권 REST API 연동 및 잔고 현황 반환
        return "키움증권 잔고 현황 (Mock)", None