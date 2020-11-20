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
allPlayers.append(GS.PlayerRole("BioFrost", 5, 7, 6, 15))
allPlayers.append(GS.PlayerRole("Bjergsen", 6, 9, 7, 19))
allPlayers.append(GS.PlayerRole("Broken_Blade", 6, 7, 7, 16))
allPlayers.append(GS.PlayerRole("DoubleLift", 7, 9, 6, 18))
allPlayers.append(GS.PlayerRole("Spica", 9, 7, 7, 17))
allPlayers.append(GS.PlayerRole("Top369", 8, 8, 9, 20))
allPlayers.append(GS.PlayerRole("JackeyLove", 8, 9, 8, 24))
allPlayers.append(GS.PlayerRole("Karsa", 7, 9, 7, 21))
allPlayers.append(GS.PlayerRole("knight", 8, 9, 9, 21))
allPlayers.append(GS.PlayerRole("QiuQui", 7, 7, 7, 15))
allPlayers.append(GS.PlayerRole("Caps", 10, 8, 10, 25))
allPlayers.append(GS.PlayerRole("Jankos", 7, 9, 7, 17))
allPlayers.append(GS.PlayerRole("Mikyx", 7, 9, 10, 22))
allPlayers.append(GS.PlayerRole("Perkz", 8, 10, 7, 22))
allPlayers.append(GS.PlayerRole("Wunder", 6, 9, 10, 17))
allPlayers.append(GS.PlayerRole("Bwipo", 7, 7, 9, 19))
allPlayers.append(GS.PlayerRole("Hylissang", 7, 10, 7, 18))
allPlayers.append(GS.PlayerRole("Nemesis", 5, 7, 6, 16))
allPlayers.append(GS.PlayerRole("Rekkles", 8, 9, 8, 24))
allPlayers.append(GS.PlayerRole("SelfMade", 10, 7, 9, 23))
allPlayers.append(GS.PlayerRole("BeryL", 8, 8, 9, 21))
allPlayers.append(GS.PlayerRole("Canyon", 8, 8, 8, 25))
allPlayers.append(GS.PlayerRole("Ghost", 7, 8, 9, 20))
allPlayers.append(GS.PlayerRole("Nuguri", 10, 8, 9, 25))
allPlayers.append(GS.PlayerRole("ShowMaker", 7, 9, 10, 22))
allPlayers.append(GS.PlayerRole("Zoom", 8, 9, 8, 22))
allPlayers.append(GS.PlayerRole("Yagao", 10, 7, 8, 22))
allPlayers.append(GS.PlayerRole("LoKeN", 7, 8, 6, 16))
allPlayers.append(GS.PlayerRole("LvMao", 7, 7, 7, 18))
allPlayers.append(GS.PlayerRole("Kanavi", 8, 10, 5, 17))
allPlayers.append(GS.PlayerRole("Bin", 9, 7, 9, 20))
allPlayers.append(GS.PlayerRole("SofM", 10, 6, 10, 25))
allPlayers.append(GS.PlayerRole("Angel", 8, 8, 8, 20))
allPlayers.append(GS.PlayerRole("Huanfeng", 10, 7, 8, 21))
allPlayers.append(GS.PlayerRole("SwordArt", 8, 10, 6, 22))
allPlayers.append(GS.PlayerRole("Rascal", 8, 8, 8, 20))
allPlayers.append(GS.PlayerRole("Clid", 6, 9, 6, 19))
allPlayers.append(GS.PlayerRole("Bdd", 7, 9, 7, 20))
allPlayers.append(GS.PlayerRole("Ruler", 8, 10, 10, 25))
allPlayers.append(GS.PlayerRole("Life", 7, 7, 7, 17))
allPlayers.append(GS.PlayerRole("Doran", 8, 7, 7, 19))
allPlayers.append(GS.PlayerRole("Pyosik", 10, 7, 8, 20))
allPlayers.append(GS.PlayerRole("Chovy", 8, 10, 8, 23))
allPlayers.append(GS.PlayerRole("Deft", 6, 10, 9, 23))
allPlayers.append(GS.PlayerRole("Keria", 7, 7, 7, 17))
allPlayers.append(GS.PlayerRole("Impact", 7, 10, 8, 20))
allPlayers.append(GS.PlayerRole("Broxah", 6, 9, 7, 18))
allPlayers.append(GS.PlayerRole("Jensen", 7, 8, 7, 18))
allPlayers.append(GS.PlayerRole("Tactical", 8, 6, 8, 16))
allPlayers.append(GS.PlayerRole("CoreJJ", 8, 10, 8, 25))



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



