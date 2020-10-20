import gameSimulator as GS





def Search(arry, value):
    for i in range(len(players1)):
        if arry[i].getExperience() == value:
            print(arry[i].getName() + " The value was found at", i + 1)
            break






players2 = []
players2.append(GS.PlayerRole("Jacob", 7, 8, 9, 19))
players2.append(GS.PlayerRole("Frank", 7, 8, 9, 19))
players2.append(GS.PlayerRole("Erik", 5, 8, 9, 14))
players2.append(GS.PlayerRole("Lars", 1, 1, 1, 1))
players2.append(GS.PlayerRole("george", 6, 2, 9, 22))





allPlayers = []

allPlayers.append(GS.PlayerRole("BioFrost", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Bjergsen", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Broken_Blade", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("DoubleLift", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Spica", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Top369", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("JackeyLove", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Karsa", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("knight", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("QiuQui", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("knight", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Caps", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Jankos", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Mikyx", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Perkz", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Wunder", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Bwipo", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Hylissang", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Nemesis", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Rekkles", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("SelfMade", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("BeryL", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Canyon", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Ghost", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("Nuguri", 5, 7, 6, 20))
allPlayers.append(GS.PlayerRole("ShowMaker", 5, 7, 6, 20))

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