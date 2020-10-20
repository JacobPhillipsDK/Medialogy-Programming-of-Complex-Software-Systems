import gameSimulator as GS
from Playerlist import playerList

def Search(arry, value):
    for i in range(len(players1)):
        if arry[i].getExperience() == value:
            print(arry[i].getName() + " The value was found at", i + 1)
            break
def sortafterCost(sorted):
    for i in range(len(allPlayers)-1,0,-1):
        for j in range(i):
            if allPlayers[j].getCost()>allPlayers[j+1].getCost():
                temp = sorted[j]
                sorted[j] = sorted[j+1]
                sorted[j+1] = temp


players1 = []
players1.append(GS.PlayerRole((Biofrost)))
players1.append(GS.PlayerRole((Biofrost)))
players1.append(GS.PlayerRole((Biofrost)))
players1.append(GS.PlayerRole((Biofrost)))
players1.append(GS.PlayerRole((Biofrost)))




players2 = []
players2.append(GS.PlayerRole("Poul", 5, 7, 6,20))
players2.append(GS.PlayerRole("Frank", 7, 8, 9,19))
players2.append(GS.PlayerRole("Erik", 5, 8, 9,14))
players2.append(GS.PlayerRole("Lars", 10, 8, 9,19))
players2.append(GS.PlayerRole("george", 6, 2, 9,22))





allPlayers = []

allPlayers.append(GS.PlayerRole("BioFrost", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Bjergsen", 6, 9, 7, 20))
allPlayers.append(GS.PlayerRole("Broken_Blade", 6, 7, 7, 20))
allPlayers.append(GS.PlayerRole("DoubleLift", 7, 9, 6, 20))
allPlayers.append(GS.PlayerRole("Spica", 9, 7, 7, 20))
allPlayers.append(GS.PlayerRole("Top369", 8, 8, 9, 20))
allPlayers.append(GS.PlayerRole("JackeyLove", 8, 9, 8, 20))
allPlayers.append(GS.PlayerRole("Karsa", 7, 9, 7, 20))
allPlayers.append(GS.PlayerRole("knight", 8, 9, 9, 20))
allPlayers.append(GS.PlayerRole("QiuQui", 7, 7, 7, 20))
allPlayers.append(GS.PlayerRole("Caps", 10, 8, 10, 20))
allPlayers.append(GS.PlayerRole("Jankos", 7, 9, 7, 20))
allPlayers.append(GS.PlayerRole("Mikyx", 7, 9, 10, 20))
allPlayers.append(GS.PlayerRole("Perkz", 8, 10, 7, 20))
allPlayers.append(GS.PlayerRole("Wunder", 6, 9, 10, 20))
allPlayers.append(GS.PlayerRole("Bwipo", 7, 7, 9, 20))
allPlayers.append(GS.PlayerRole("Hylissang", 7, 10, 7, 20))
allPlayers.append(GS.PlayerRole("Nemesis", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Rekkles", 8, 9, 8, 20))
allPlayers.append(GS.PlayerRole("SelfMade", 10, 7, 9, 20))
allPlayers.append(GS.PlayerRole("BeryL", 8, 8, 9, 20))
allPlayers.append(GS.PlayerRole("Canyon", 8, 8, 8, 20))
allPlayers.append(GS.PlayerRole("Ghost", 7, 8, 9, 20))
allPlayers.append(GS.PlayerRole("Nuguri", 10, 8, 9, 20))
allPlayers.append(GS.PlayerRole("ShowMaker", 7, 9, 10, 20))

players2 = []
players2.append(allPlayers[16])
players2.append(allPlayers[12])
players2.append(allPlayers[11])
players2.append(allPlayers[9])
players2.append(allPlayers[17])



players1 = []
players1.append(allPlayers[2])
players1.append(allPlayers[3])
players1.append(allPlayers[7])
players1.append(allPlayers[10])
players1.append(allPlayers[15])

redteam = GS.Team("red FC", players1)
blueteam = GS.Team("blue FC", players2)

game = GS.gameSimulator()
game.game_start(blueteam, redteam)


for i in range(len(players1) - 1, 0, -1):
    for j in range(i):
        if players1[j].getExperience() > players1[j + 1].getExperience():
            players1[j], players1[j + 1] = players1[j + 1], players1[j]

for i in range(len(players1)):
    print(players1[i].getName())


value = 15

for i in range(len(players1)):
    if players1[i].getCost() == value:
        print(players1[i].getName() + " The value was found at", i + 1)
        break
print(players1[0].getName())
sortafterCost(allPlayers)
print(allPlayers[0].getName())