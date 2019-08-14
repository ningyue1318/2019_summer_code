import sys
sys.path.append('..')
import logging
from functools import wraps
import datetime
from conf.settings import LOG_DIR


def log_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(format='%(asctime)s  %(message)s',
                            filename=LOG_DIR,
                            level=logging.DEBUG)
        logging.info(func.__name__+" function perform")
        return func(*args, **kwargs)

    return wrapper
