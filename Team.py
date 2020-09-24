import PlayerRole

class Team:
    __name = "LoL team"
    __playerSupp = PlayerRole
    __playerAdc = PlayerRole
    __playerMid = PlayerRole
    __playerJung = PlayerRole
    __playerTop = PlayerRole

    def __init__(self, supp: PlayerRole, adc: PlayerRole, mid: PlayerRole, jung: PlayerRole, top: PlayerRole):
        self.__supp = supp
        self.__adc = adc
        self.__mid = mid
        self.__jung = jung
        self.__top = top

    def getMotivationAvg(self):
        total = 0
        total = self.__playerSupp.getMotivation() + self.__playerAdc.getMotivation() + self.__playerJung.getMotivation() + self.__playerMid.getMotivation() + self.__playerTop.getMotivation()
        return total / 5

    def getExperienceAvg(self):
        total = 0
        total = self.__playerSupp.getExperience() + self.__playerAdc.getExperience() + self.__playerJung.getExperience() + self.__playerMid.getExperience() + self.__playerTop.getExperience()
        return total / 5


