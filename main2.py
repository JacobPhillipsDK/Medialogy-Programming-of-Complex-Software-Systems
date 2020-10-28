import gameSimulator as GS

<<<<<<< Updated upstream

def Search(arry, value):
    for i in range(len(players1)):
        if arry[i].getName() == value:
            print(arry[i].getName())
=======
def Search(list, value):
    for i in range(len(players1)):
        if list[i].getCost() == value:
            print(list[i].getName() + " The value was found at", i + 1)
>>>>>>> Stashed changes
            break


def sortafterCost(sorted):
    for i in range(len(allPlayers) - 1, 0, -1):
        for j in range(i):
<<<<<<< Updated upstream
            if allPlayers[j].getCost() > allPlayers[j + 1].getCost():
                sorted[j], sorted[j + 1] = sorted[j + 1], sorted[j]

=======
            if allPlayers[j].getCost()>allPlayers[j+1].getCost():
                sorted[j], sorted[j+1] = sorted[j+1], sorted[j]
>>>>>>> Stashed changes

allPlayers = []

allPlayers.append(GS.PlayerRole("BioFrost", 5, 7, 6, 5))
allPlayers.append(GS.PlayerRole("Bjergsen", 6, 9, 7, 7))
allPlayers.append(GS.PlayerRole("Broken_Blade", 6, 7, 7, 9))
allPlayers.append(GS.PlayerRole("DoubleLift", 7, 9, 6, 2))
allPlayers.append(GS.PlayerRole("Spica", 9, 7, 7, 8))
allPlayers.append(GS.PlayerRole("Top369", 8, 8, 9, 13))
allPlayers.append(GS.PlayerRole("JackeyLove", 8, 9, 8, 17))
allPlayers.append(GS.PlayerRole("Karsa", 7, 9, 7, 19))
allPlayers.append(GS.PlayerRole("knight", 8, 9, 9, 20))
allPlayers.append(GS.PlayerRole("QiuQui", 7, 7, 7, 20))
allPlayers.append(GS.PlayerRole("Caps", 10, 8, 10, 20))
allPlayers.append(GS.PlayerRole("Jankos", 7, 9, 7, 20))
allPlayers.append(GS.PlayerRole("Mikyx", 7, 9, 10, 20))
allPlayers.append(GS.PlayerRole("Perkz", 8, 10, 7, 20))
allPlayers.append(GS.PlayerRole("Wunder", 6, 9, 10, 8))
allPlayers.append(GS.PlayerRole("Bwipo", 7, 7, 9, 20))
allPlayers.append(GS.PlayerRole("Hylissang", 7, 10, 7, 11))
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


<<<<<<< Updated upstream
for i in range(len(players1) - 1, 0, -1):
    for j in range(i):
        if players1[j].getCost() > players1[j + 1].getCost():
            players1[j], players1[j + 1] = players1[j + 1], players1[j]

sortafterCost(allPlayers)
for i in range(len(allPlayers)):
    print(allPlayers[i].getName())
=======
sortafterCost(allPlayers)
for i in range(len(allPlayers)):
    print(allPlayers[i].getName())

Search(allPlayers,20)
>>>>>>> Stashed changes
