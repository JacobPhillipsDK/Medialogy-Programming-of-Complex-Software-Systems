import gameSimulator as GS


def Search(arry, value):
    for i in range(len(players1)):
        if arry[i].getExperience() == value:
            print(arry[i].getName() + " The value was found at", i + 1)
            break

players1 = []
players1.append(GS.PlayerRole("Kristian", 8, 8, 9,15))
players1.append(GS.PlayerRole("Jacob", 2, 3, 4,6))
players1.append(GS.PlayerRole("Nicklas", 6, 8, 6,13))
players1.append(GS.PlayerRole("Mikkel", 7, 9, 5,12))
players1.append(GS.PlayerRole("Lukas", 6, 10, 5,18))

players2 = []
players2.append(GS.PlayerRole("Poul", 5, 7, 6,20))
players2.append(GS.PlayerRole("Frank", 7, 8, 9,19))
players2.append(GS.PlayerRole("Erik", 5, 8, 9,14))
players2.append(GS.PlayerRole("Lars", 10, 8, 9,19))
players2.append(GS.PlayerRole("george", 6, 2, 9,22))

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

