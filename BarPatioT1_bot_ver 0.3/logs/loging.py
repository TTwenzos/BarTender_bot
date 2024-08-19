from loguru import logger

logger.add("info.log", format = "{time} {level} {message}", level = "INFO", rotation='10 mb', compression=zip)
logger.add('exception.log', format = "{time} {level} {message}", level = "WARNING", rotation='10 mb', compression=zip)
logger.add('Critical.log', format = "{time} {level} {message}", level = "CRITICAL", rotation='10 mb', compression=zip)

def info_logger(message: str):
    logger.info(message)

def Exception_logger(filename, error, level = 'info'):
    INFO = ('INFO', "I", "info", 'i')
    ERROR = ('ERROR', "ERR", "E", 'error', 'err', 'e')
    CRITICAL = ("CRITICAL", "C", "CRIT", "critical", 'c', 'crit')
    error_str = f"File: {filename}, error code: {error}!"
    if level in INFO:
        logger.info(error_str)
    elif level in ERROR:
        logger.error(error_str)
    elif level in CRITICAL:
        logger.critical(error_str)
    else: logger.info(f"Error level not defined: {error_str} ")

def feedback(message):
    user = f"{message.from_user.first_name} {message.from_user.last_name} ({message.from_user.username})"
    if len(message.text) <= 200:
        feedback_text = message.text
        logger.info(f'Пользователь:{user}, оставил сообщение: {feedback_text}')