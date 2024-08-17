from loguru import logger

logger.add("debug.log", format = "{time} {level} {message}", level = "DEBUG")

def err_archivist(filename, error, level = 'info'):
    INFO = ('INFO', "I", "info", 'i')
    DEBUG = ("DEBUG", "D", 'debug', "d")
    ERROR = ('ERROR', "ERR", "E", 'error', 'err', 'e')
    CRITICAL = ("CRITICAL", "C", "CRIT", "critical", 'c', 'crit')
    error_str = f"File: {filename}, error code: {error}!"
    if level in INFO:
        logger.info(error_str)
    elif level in DEBUG:
        logger.debug(error_str)
    elif level in ERROR:
        logger.error(error_str)
    elif level in CRITICAL:
        logger.critical(error_str)
    else: logger.info(f"Error level not defined: {error_str} ")