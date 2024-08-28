
# Импорты сторонних библиотек || Смотрите фаил property.toml
from loguru import logger

logus = logger # Просто, чтобы не импортировать loguru в каждый фаил

# Журнал записи обратной связи от пользователей из бота.
logger.level("FEEDBACK", no=5, color="<magenta>", icon="♻️")
class get_logs():
  logger.add("Logs\\FeedBack\\FEEDBACK.log",
            format = "{time} {level} {message}",
            level = "FEEDBACK",
            rotation='10 mb', 
            compression=zip,
            filter=lambda x: '[FEEDBACK]' in x['message'])
  # Запись хода выполнения программы бота.
  logger.add("Logs\\INFO.log",
            format = "{time} {level} {message}",
            level = "INFO", 
            rotation='10 mb', 
            compression=zip,
            filter=lambda x: '[INFO]' in x['message'])
  # Журнал выполнения ботом базовых функций.
  logger.add("Logs\\SUCCESS.log",
            format = "{time} {level} {message}",
            level = "INFO", 
            rotation='10 mb', 
            compression=zip,
            filter=lambda x: '[SUCCESS]' in x['message'])
  # Журнал сбоев в коде, не мешающих его исполнению.
  logger.add("Logs\\WARNING.log",
            format = "{time} {level} {message}",
            level = "INFO", 
            rotation='10 mb', 
            compression=zip,
            filter=lambda x: '[WARNING]' in x['message'])
  #  Критические ошибки, невыполнение функций ботом
  logger.add("Logs\\ERROR.log",
            format = "{time} {level} {message}",
            level = "INFO", 
            rotation='10 mb', 
            compression=zip,
            filter=lambda x: '[ERROR]' in x['message'])
  #  Ошибки из-за которых бот упал
  logger.add("Logs\\CRITICAL.log",
            format = "{time} {level} {message}",
            level = "INFO", 
            rotation='10 mb', 
            compression=zip,
            filter=lambda x: '[CRITICAL]' in x['message'])


def logoose(filename, message, level):
    loglevel = {
    "FEEDBACK": ('FEEDBACK', 'F', 'feedback', 'f'),
    "INFO": ('INFO', "I", "info", 'i'),
    "SUCCESS": ('SUCCESS', 'S', 'success', 's'),
    "ERROR": ('ERROR', "ERR", "E", 'error', 'err', 'e'),
    "WARNING": ('WARNING', 'W', 'warning', 'w'),
    "CRITICAL": ("CRITICAL", "C", "CRIT", "critical", 'c', 'crit')}
    for i in loglevel:
      if level in loglevel[i]:
        string = f'[{i}]|| File: {filename} — {message}'
        logger.log(i, string)

