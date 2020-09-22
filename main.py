import logging

# https://docs.python.org/3/howto/logging.html - Loggin meaning

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Just logger")


if __name__ == '__main__':
    main()
