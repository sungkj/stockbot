import yaml
import datetime
from telegram.ext import Application
from utils.logger import setup_logger
from tasks.news_monitor import NewsMonitor
from tasks.google_trends import GoogleTrendsTask
from tasks.kiwoom_api import KiwoomApiTask

logger = setup_logger(__name__)

class TaskManager:
    def __init__(self, bot_app: Application, config_path="config.yaml"):
        self.bot_app = bot_app
        self.job_queue = self.bot_app.job_queue
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    def start_tasks(self):
        logger.info("Starting tasks...")
        
        # 1. 구글 트렌드 분석 (스케줄링 예시: 매일 1회)
        trends_task = GoogleTrendsTask()
        self.job_queue.run_repeating(
            self._wrap_task(trends_task.run),
            interval=86400, # 24시간
            first=10 # 시작 후 10초 뒤 최초 실행
        )
        
        # 2. 실시간 뉴스 모니터링 (반복 예시: 1분마다)
        news_task = NewsMonitor()
        self.job_queue.run_repeating(
            self._wrap_task(news_task.run),
            interval=60, # 60초 간격
            first=5
        )
        
        # 3. 키움증권 데이터 및 스케줄러 설정
        kiwoom_task = KiwoomApiTask()
        kst = datetime.timezone(datetime.timedelta(hours=9)) # KST (UTC+9)
        
        # 3-1. 평일(월~금) 15시 40분마다 계좌 요약 자동 발송
        self.job_queue.run_daily(
            self._wrap_task(kiwoom_task.run),
            time=datetime.time(hour=15, minute=40, tzinfo=kst),
            days=(0, 1, 2, 3, 4) # 0:월요일 ~ 4:금요일
        )

        # 3-2. 매일 새벽 3시에 전체 계좌 토큰 자동 재발급
        async def reissue_token_wrapper(context):
            logger.info("새벽 3시: 키움증권 토큰 재발급 시작")
            try:
                await kiwoom_task.initialize()
                user_id = self.config["telegram"]["user_id"]
                await context.bot.send_message(chat_id=user_id, text="🔄 [시스템] 키움증권 API 접속 토큰이 갱신되었습니다.")
            except Exception as e:
                logger.error(f"키움증권 토큰 재발급 실패: {e}")

        self.job_queue.run_daily(
            reissue_token_wrapper,
            time=datetime.time(hour=3, minute=0, tzinfo=kst)
        )

    def _wrap_task(self, task_func):
        """각 Task를 실행하고 결과를 텔레그램으로 전송하는 래퍼 함수"""
        async def wrapper(context):
            user_id = self.config["telegram"]["user_id"]
            try:
                message, photo = await task_func()
                if message or photo:
                    if photo:
                        await context.bot.send_photo(chat_id=user_id, photo=photo, caption=message)
                    else:
                        await context.bot.send_message(chat_id=user_id, text=message)
            except Exception as e:
                logger.error(f"Task failed: {e}")
        return wrapper