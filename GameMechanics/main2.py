from GameMechanics import gameSimulator as GS


def Search(arry, value):
    for i in range(len(players1)):
        if arry[i].getName() == value:
            print(arry[i].getName())


def SearchCost(list, value):
    for i in range(len(players1)):
        if list[i].getCost() == value:
            print(list[i].getName() + " The value was found at", i + 1)


def sortafterCost(sorted):
    for i in range(len(allPlayers) - 1, 0, -1):
        for j in range(i):
            if allPlayers[j].getExperience() > allPlayers[j + 1].getExperience():
                sorted[j], sorted[j + 1] = sorted[j + 1], sorted[j]


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
allPlayers.append(GS.PlayerRole("ShowMaker", 7, 9, 10, 30))

players2 = []
players2.append(allPlayers[16])
players2.append(allPlayers[12])
players2.append(allPlayers[11])
players2.append(allPlayers[9])
players2.append(allPlayers[17])

players1 = []
players1.append(allPlayers[16])
players1.append(allPlayers[12])
players1.append(allPlayers[11])
players1.append(allPlayers[9])
players1.append(allPlayers[17])

def startGame():
    redteam = GS.Team("red FC", players1)
    blueteam = GS.Team("blue FC", players2)
    game = GS.gameSimulator()
    game.game_start(blueteam, redteam)

startGame()