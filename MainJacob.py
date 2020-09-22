import logging
import numpy as np

# https://docs.python.org/3/howto/logging.html - Loggin meaning

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Just logger")


if __name__ == '__main__':
    main()


# str = string
# Class for player
class Player:
    __name = "Default"
    __Lane = "Default"

    def setName(self, new_name: str) -> None:
        self.__name = new_name

    def getName(self) -> str:
        return self.__name

    def setLane(self, new_lane: str) -> None:
        self.__Lane = new_lane

    def getLane(self) -> str:
        return self.__Lane
