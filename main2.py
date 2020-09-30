import gameSimulator as GS

players1 = []
players1.append(GS.PlayerRole("Kristian", "mid", 8,8,9))
players1.append(GS.PlayerRole("Jacob","supp",2,3,4))
players1.append(GS.PlayerRole("Nicklas","adc",6,8,6))
players1.append(GS.PlayerRole("Mikkel","jung",7,9,5))
players1.append(GS.PlayerRole("Lukas","top",6,8,5))

players2 = []
players2.append(GS.PlayerRole("Poul", "mid", 5,7,6))
players2.append(GS.PlayerRole("Frank", "supp", 7,8,9))
players2.append(GS.PlayerRole("Erik", "adc", 5,8,9))
players2.append(GS.PlayerRole("Lars", "jung", 10,8,9))
players2.append(GS.PlayerRole("george", "top", 6,2,9))

redteam = GS.Team("red FC", players1)
blueteam = GS.Team("blue FC", players2)

game = GS.gameSimulator()
game.game_start(blueteam,redteam)
