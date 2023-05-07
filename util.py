import logging


def call_logger(f):
    def log_write(c):
        logging.info(f"{f.__name__} was called with {c}")
        f(c)

    return log_write
