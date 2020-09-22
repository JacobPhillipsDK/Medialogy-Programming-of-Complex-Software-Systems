import logging
import random
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

    def __init__(self, new_name="Default", new_lane="Default"):
        self.__name = new_name
        self.__Lane = new_lane

    def setName(self, new_name: str) -> None:
        self.__name = new_name

    def getName(self) -> str:
        return self.__name

    def setLane(self, new_lane: str) -> None:
        self.__Lane = new_lane

    def getLane(self) -> str:
        return self.__Lane


class PlayerRole(Player):
    def __init__(self, new_name="Default", new_lane="Default", new_team="None", new_experience=0):
        super(Player, self).__init__(new_name, new_lane)
        self.__team = new_team
        self.__experience = new_experience

    def setLaneMid(self, midLane: str) -> None:
        self.__Lane = midLane
