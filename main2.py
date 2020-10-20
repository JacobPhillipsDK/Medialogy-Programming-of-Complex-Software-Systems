import gameSimulator as GS

Biofrost = ("BioFrost", 5, 7, 6, 20)
Bjergsen = ("Bjergsen", 5, 7, 6, 20)
Broken_Blade = ("Broken_Blade", 5, 7, 6, 20)
DoubleLift = ("DoubleLift", 5, 7, 6, 20)
Spica = ("Spica", 5, 7, 6, 20)
Top369 = ("Top369", 5, 7, 6, 20)
JackeyLove = ("JackeyLove", 5, 7, 6, 20)
Karsa = ("Karsa", 5, 7, 6, 20)
knight = ("knight", 5, 7, 6, 20)
QiuQui = ("QiuQui", 5, 7, 6, 20)
knight = ("knight", 5, 7, 6, 20)
Caps = ("Caps", 5, 7, 6, 20)
Jankos = ("Jankos", 5, 7, 6, 20)
Mikyx = ("Mikyx", 5, 7, 6, 20)
Perkz = ("Perkz", 5, 7, 6, 20)
Wunder = ("Wunder", 5, 7, 6, 20)
Bwipo = ("Bwipo", 5, 7, 6, 20)
Hylissang = ("Hylissang", 5, 7, 6, 20)
Nemesis = ("Nemesis", 5, 7, 6, 20)
Rekkles = ("Rekkles", 5, 7, 6, 20)
SelfMade = ("SelfMade", 5, 7, 6, 20)
BeryL = ("BeryL", 5, 7, 6, 20)
Canyon = ("Canyon", 5, 7, 6, 20)
Ghost = ("Ghost", 5, 7, 6, 20)
Nuguri = ("Nuguri", 5, 7, 6, 20)
ShowMaker = ("ShowMaker", 5, 7, 6, 20)




def Search(arry, value):
    for i in range(len(players1)):
        if arry[i].getExperience() == value:
            print(arry[i].getName() + " The value was found at", i + 1)
            break


players1 = []
players1.append(GS.PlayerRole((Biofrost)))
players1.append(GS.PlayerRole((Biofrost)))
players1.append(GS.PlayerRole((Biofrost)))
players1.append(GS.PlayerRole((Biofrost)))
players1.append(GS.PlayerRole((Biofrost)))


players2 = []
players2.append(GS.PlayerRole("Jacob", 7, 8, 9, 19))
players2.append(GS.PlayerRole("Frank", 7, 8, 9, 19))
players2.append(GS.PlayerRole("Erik", 5, 8, 9, 14))
players2.append(GS.PlayerRole("Lars", 1, 1, 1, 1))
players2.append(GS.PlayerRole("george", 6, 2, 9, 22))

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
