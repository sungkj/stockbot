import asyncio
from core.bot_app import TeleBotApp
from core.task_manager import TaskManager
from utils.logger import setup_logger

logger = setup_logger(__name__)

async def main():
    logger.info("Starting Telebot...")
    
    # 메인 봇 앱 초기화
    bot_app = TeleBotApp()
    
    # Task Manager 초기화 및 작업 시작 (스케줄러/모니터링)
    task_manager = TaskManager(bot_app.application)
    task_manager.start_tasks()
    
    # 봇 폴링 시작 (비동기 무한 루프)
    await bot_app.start()

if __name__ == "__main__":
    asyncio.run(main())