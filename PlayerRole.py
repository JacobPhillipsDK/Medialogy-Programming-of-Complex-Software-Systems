from Player import Player


class PlayerRole(Player):
    def __init__(self, new_name="Default", new_lane="Default", new_team="None", new_motivation=0, new_experience = 0, new_reaction = 0):
        super(Player, self).__init__(new_name, new_lane)
        self.__team = new_team
        self.__motivation = new_motivation
        self.__kills = 0
        self.__experience = new_experience
        self.__reaction = new_reaction

    def getMotivation(self):
        return self.__motivation

    def getExperience(self):
        return self.__experience

    def getReaction(self):
        return self.__reaction

    def trykill(self):
        kill = self.getExperience() * (self.getMotivation()*0.5)
        if kill >= self.getReaction()
            return True
        else
            return False

