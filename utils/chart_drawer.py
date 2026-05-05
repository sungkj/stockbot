import matplotlib.pyplot as plt
import os
from utils.logger import setup_logger

logger = setup_logger(__name__)

def draw_line_chart(data: dict, title: str, filename: str = "chart.png") -> str:
    """구글 트렌드 등의 시계열 데이터를 시각화하고 이미지 경로를 반환합니다."""
    try:
        x = list(data.keys())
        y = list(data.values())
        
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, marker='o')
        plt.title(title)
        plt.xlabel("Date/Time")
        plt.ylabel("Value")
        plt.grid(True)
        
        plt.savefig(filename)
        plt.close()
        return filename
    except Exception as e:
        logger.error(f"Error drawing chart: {e}")
        return None