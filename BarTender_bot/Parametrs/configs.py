
# Импорты встроенных библиотек 
import os
import sys
# Импорты сторонних библиотек || Смотрите фаил property.toml
from dotenv import load_dotenv
from loguru import logger

os_path = str(sys.path[0]) # Системный каталог
load_dotenv(f'{os_path}\\Bartender_bot\\Parametrs\\.env')
# Токен бота
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# File path
BL_xlsx_path = f"{os_path}\\.xlsx\\Bottle list.xlsx"
BL_db_path = f"{os_path}\\BarTender_bot\\Data Bases\\Bottle list.db"