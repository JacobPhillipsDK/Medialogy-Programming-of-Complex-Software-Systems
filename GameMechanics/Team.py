from GameMechanics.PlayerRole import *
from typing import List

class Team:
    __name = "LoL team"
    __players = []

    def __init__(self, name: str, players: List[PlayerRole]):
        self.__name = name
        self.__players = players

    for i in range(5):
        __players.append(PlayerRole("faker",5,7,9,1))

    def get_Player(self, num: int):
        return self.__players[num]

    def getMotivationAvg(self) -> int:
        total = 0
        for i in range(5):
            total += self.__players[i].getMotivation()
        return total / 5

    def getExperienceAvg(self) -> int:
        total = 0
        for i in range(5):
            total += self.__players[i].getExperience()
        return total / 5

    def getName(self):
        return self.__name



