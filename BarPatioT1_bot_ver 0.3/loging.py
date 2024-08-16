from loguru import logger

logger.add("debug.log", format = "{time} {level} {message}", level = "DEBUG")

def err_archivist(filename, error):
    error_str = f"File: {filename}, error code: {error}!"
    logger.debug(error_str)