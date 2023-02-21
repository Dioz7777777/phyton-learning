import logging


logging.basicConfig(level=logging.DEBUG)


def debug(message: str, *args) -> None:
    logging.debug(message, *args)
