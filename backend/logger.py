import logging

def setup_logger():
    logger = logging.getLogger('jarvis_logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('jarvis.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
