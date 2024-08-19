from logs.loging import Exception_logger
from dotenv import load_dotenv
import sys
import os

os_path = str(sys.path[0]) # Системный каталог

load_dotenv(f'{os_path}\\.env')

try:
#  Токен телеграм бота
  TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

#  Другие переменные окружения
  ROOT_PASS = os.getenv("TELEGRAM_BOT_ROOT_PASSWORD")
except Exception as e:
  Exception_logger(__name__, e, 'c')

# Пути файлов

bottle_list_path = f"{os_path}\\Files\\Libs\\Bottle list.xlsx" 
