from Player import Player
from numpy import random
from ChampionPicker import *

class PlayerRole(Player):
    __motivation = 1
    __experience = 1

    def __init__(self, new_name: str, new_motivation: int, new_experience: int, new_reaction: int):
        Player.__init__(self, new_name)
        self.__motivation = new_motivation
        self.__experience = new_experience
        self.__reaction = new_reaction

    def getMotivation(self) -> int:
        return self.__motivation

    def getExperience(self) -> int:
        return self.__experience

    def getReaction(self) -> int:
        return self.__reaction

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
