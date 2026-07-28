from loguru import logger
import os

os.makedirs("logs", exist_ok=True)

logger.add(
    "logs/datapilot.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
    enqueue=True,
)

app_logger = logger