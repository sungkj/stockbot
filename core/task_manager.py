import yaml
from telegram.ext import Application
from utils.logger import setup_logger
from tasks.news_monitor import NewsMonitor
from tasks.google_trends import GoogleTrendsTask

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