from PlayerRole import *
from typing import List

class Team:
    __name = "LoL team"
    __players = []


    def __init__(self, name: str, players: List[PlayerRole]):
        self.__name = name
        self.__players = players

    for i in range(5):
        __players.append(PlayerRole("faker","mid",5,7,9))

    def get_Player(self, num: int):
        return self.__players[num]

    def getMotivationAvg(self):
        total = 0
        total = self.__playerSupp.getMotivation() + self.__playerAdc.getMotivation() + self.__playerJung.getMotivation() + self.__playerMid.getMotivation() + self.__playerTop.getMotivation()
        return total / 5

    def getExperienceAvg(self):
        total = 0
        total = self.__playerSupp.getExperience() + self.__playerAdc.getExperience() + self.__playerJung.getExperience() + self.__playerMid.getExperience() + self.__playerTop.getExperience()
        return total / 5

    def getName(self):
        return self.__name



