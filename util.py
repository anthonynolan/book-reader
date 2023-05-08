import logging


def call_logger(f):
    def log_write(*args):
        logging.info(f"{f.__name__} was called with {args}")
        return f(args)

    return log_write
