from Team import *
import numpy as np
from ChampionPicker import *
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

    def game_start(self,blueteam: Team, redteam: Team):
        self.__blueSideteam = blueteam.getName()
        self.__redSideteam = redteam.getName()
        self.__killsBlue = 0
        self.__killsRed = 0

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
                ptk = blueteam




 def StartGame(self):
        pickamp = SetTeam(setblueteam(), setredteam())



