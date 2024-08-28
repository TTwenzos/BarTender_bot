
# Импорты встроенных библиотек 
import sys
import os
# Импорты сторонних библиотек || Смотрите фаил property.toml
from dotenv import load_dotenv
from loguru import logger
os_path = str(sys.path[0]) # Системный каталог
load_dotenv(f'{os_path}\\Bartender_bot\\Parametrs\\.env')
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
logger.debug(f'{os_path}\\Parametrs\\.env')
