from config import *
from constans import *
from loguru import logger
from logs.loging import info_logger
import os

logger.catch()
def root(user: str,password: str) -> bool:
  if password == ROOT_PASS:
    info_logger(f'Пользователь:{user} — получил права администратора')
    os.environ['SUPERUSER_RIGHT'] = 'True'
    logger.debug(os.environ.get('SUPERUSER_RIGHT'))
    return True
  else: 
    info_logger(f'Пользователь:{user} — пытался получить права администратора')
    os.environ['SUPERUSER_RIGHT'] = 'False'
    return False