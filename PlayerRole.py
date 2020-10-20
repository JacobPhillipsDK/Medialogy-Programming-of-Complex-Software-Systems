from Player import Player
from numpy import random
from ChampionPicker import *

class PlayerRole(Player):
    __motivation = 1
    __experience = 1
    __cost = 1 #0-25

    def __init__(self, new_name: str, new_motivation: int, new_experience: int, new_reaction: int, new_cost: int):
        Player.__init__(self, new_name)
        self.__motivation = new_motivation
        self.__experience = new_experience
        self.__reaction = new_reaction
        self.__cost = new_cost
        self.__name = new_name

    def getMotivation(self) -> int:
        return self.__motivation

    def getExperience(self) -> int:
        return self.__experience

    def getReaction(self) -> int:
        return self.__reaction

    def getCost(self) -> int:
        return self.__cost

    def tryKill(self, deaf: int) -> bool:
        r = random.randint(-2, 2)
        kill = self.getExperience() + self.getMotivation() + r
        if kill >= deaf:
            return True
        else:
            return False

    def trydeff(self) -> int:
        r1 = random.randint(-2, 2)
        deaf = self.getExperience() + self.getReaction() + r1
        return deaf

    def getName(self) -> str:
        return self.__name