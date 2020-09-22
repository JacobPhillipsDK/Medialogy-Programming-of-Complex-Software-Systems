from Player import Player


class PlayerRole(Player):
    def __init__(self, new_name="Default", new_lane="Default", new_team="None", new_experience=0):
        super(Player, self).__init__(new_name, new_lane)
        self.__team = new_team
        self.__experience = new_experience
        self.__kills = 0
