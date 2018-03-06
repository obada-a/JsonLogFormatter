import logging, sys

from json_formatter import formatter

logger = logging.Logger(__name__)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter.JSONFormatter())

logger.addHandler(handler)


def throw_exception():
    raise ValueError('Some exception')


if __name__ == '__main__':
    try:
        throw_exception()
    except Exception as e:
        logger.error(e, exc_info=True)
