from Team import *
import numpy as np
#from ChampionPicker import *
from numpy import random

class gameSimulator:
    __blueSideteam = "A"
    __redSideteam = "B"
    __killsBlue = 0
    __killsRed = 0

    def get_blue_team(self):
        return self.__blueSideteam

    def get_red_team(self):
        return self.__redSideteam

    def get_kills_blue(self):
        return self.__killsBlue

    def get_kills_red(self):
        return self.__killsRed

    def game_result(self):
        print("This epic League of Legends game ends with the results: \n" + self.__blueSideteam + " - " + str(self.__killsBlue)
              + self.__redSideteam + " - " + str(self.__killsRed))

    #def StartGame(self):
        #pickamp = SetTeam(setblueteam(), setredteam())

    def game_start(self,blueteam: Team, redteam: Team):
        self.__blueSideteam = blueteam.getName()
        self.__redSideteam = redteam.getName()
        self.__killsBlue = 0
        self.__killsRed = 0

        self.StartGame()

        gameRuns = True
        gameTime = 40 + random.int(-5,5)
        Time = 1

        while gameRuns:
            nextKill = random.randint(0,6)
            if(Time+nextKill > gameTime or Time > gameTime):
                #Stops the game when it goes over the game time
                break

            Time += nextKill

            blueSkill = blueteam.getExperienceAvg() + blueteam.getMotivationAvg()
            redSkill = redteam.getExperienceAvg() + redteam.getMotivationAvg()

            playerNum = random.randint(0,5)

            if random.randint(int(-blueSkill),int(redSkill)) <= 0:
                bptk = blueteam.get_Player(playerNum)
                rptd = redteam.get_Player(playerNum)
                deff = rptd.trydeff()
                kill = bptk.tryKill(deff)
                if kill == True:
                    killSuccess = True
                else:
                    killSuccess = False

                print(str(Time) + ":" + "Seems like a blueteam player is trying to kill a redteam player")

                if killSuccess:
                    self.__killsBlue = +1
                    print("And blueteam player is succesfull, what a kill!")
                else:
                    print("redteam player defends, very nice!")
            else:
                bptk = blueteam.get_Player(playerNum)
                rptd = redteam.get_Player(playerNum)
                deff = bptk.trydeff()
                kill = rptd.tryKill(deff)
                if kill == True:
                    killSuccess = True
                else:
                    killSuccess = False

                print(str(Time) + ":" + "Seems like a blueteam player is trying to kill a redteam player")

                if killSuccess:
                    self.__killsRed = +1
                    print("And redteam player is succesfull, what a kill!")
                else:
                    print("blueteam player defends, very nice!")













