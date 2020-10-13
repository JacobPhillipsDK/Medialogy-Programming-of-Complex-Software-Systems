debug = False
import gameSimulator as GS
from ChampionPicker import *
#
players1 = []
players1.append(GS.PlayerRole("Kristian", "top", 8, 8, 9))
players1.append(GS.PlayerRole("Jacob", "supp", 10, 10, 10))
players1.append(GS.PlayerRole("Nicklas", "adc", 6, 8, 6))
players1.append(GS.PlayerRole("Mikkel", "jung", 7, 9, 5))
players1.append(GS.PlayerRole("Lukas", "top", 6, 8, 5))

players2 = []
players2.append(GS.PlayerRole("Poul", "mid", 5, 7, 6))
players2.append(GS.PlayerRole("Frank", "supp", 7, 8, 9))
players2.append(GS.PlayerRole("Erik", "adc", 5, 8, 9))
players2.append(GS.PlayerRole("Lars", "jung", 2, 2, 2))
players2.append(GS.PlayerRole("george", "top", 6, 2, 9))

redteam = GS.Team("red FC", players1)
blueteam = GS.Team("blue FC", players2)

print('Welcome to League of legends simulator')

UserInput = 0
while UserInput not in ['1', '2']:
    print("""
            1 - Battle against computer    
            2 - Battle against other player""")
    UserInput = input()
    if UserInput not in ['1', '2']:
        print('Enter a Valid input')

if UserInput == '1':
    game = GS.gameSimulator()
    game.game_start(blueteam, redteam)

if UserInput == '2':
    print("Started work against other player")

if debug:
    print(UserInput)
