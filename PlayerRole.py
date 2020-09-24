from Player import Player
from numpy import random


class PlayerRole(Player):
    def __init__(self, new_name="Default", new_lane="Default", new_team="None", new_motivation=0, new_experience=0,
                 new_reaction=0):
        Player.__init__(self, new_name, new_lane)
        self.__team = new_team
        self.__motivation = new_motivation
        self.__experience = new_experience
        self.__reaction = new_reaction

    def getMotivation(self) -> int:
        return self.__motivation

    def getExperience(self) -> int:
        return self.__experience

    def getReaction(self) -> int:
        return self.__reaction

<<<<<<< Updated upstream
    def tryKill(self, PlayerRole):
=======


    def trykill(self, defff: int) -> bool:
>>>>>>> Stashed changes
        r = random.randint(-2, 2)
        kill = self.getExperience() + (self.getMotivation()) + r
        if kill >= self.trydeff():
            return True
        else:
            return False


    def trydeff(self) -> int:
        r1 = random.randint(-2,2)
        deff = self.getExperience() + self.getReaction() + r1
        return deff

