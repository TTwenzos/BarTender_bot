from loguru import logger

logger.add("debug.log", format = "{time} {level} {message}", level = "DEBUG")

def err_archivist(filename, error, level = 'degug'):
    error_str = f"File: {filename}, error code: {error}!"
    if level == 'debug':
        logger.debug(error_str)
    elif level == "error":
        logger.error(error_str)
    elif level == 'CRITICAL':
        logger.critical(error_str)