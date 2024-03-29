import logging


def get_logger(name) -> logging:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    formatter = logging.Formatter('[%(asctime)s] %(levelname)s(%(name)s) : %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
