import socket
from main2 import *
import threading
import pickle
from GameMechanics import gameSimulator as GS
global playerNames
global USER_COUNT

# 64 byte
HEADER = 64
# Port
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# Adress
ADDR = (SERVER, PORT)
# Hvilken formatering den er I
FORMAT = 'utf-8'
# Hvis en person sender denne besked, vil clienten bliver afbrudt fra serveren.
DISCONNECT_MESSAGE = "!DISCONNECT"

# String saved for Teams.


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)



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

players1 = []
players2 = []

player11 = str("Player")

def StartGameMultiplayer():
    Player1 = GS.Team("Player 1", players1)
    Player2 = GS.Team("PLayer 2", players2)
    game = GS.gameSimulator()
    game.game_start(Player1, Player2)

# Gør det mulig at sende beskeder til client som string format i console
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        # Siger længden af beskeden er 64 byte og skal formateres som utf-8
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send(f"[SERVER] You have connected to {SERVER}".encode(FORMAT))
            conn.send(f"[SERVER]  Test")
    conn.close()


# Starer socket server
# Lytter efter forbindelse anmodninger
def start():
    server.listen(2)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]   {threading.active_count() - 1}")
        USER_COUNT = int((threading.active_count() - 1))
        print(f"[ACTIVE USER_COUNT:]   {USER_COUNT}")
        if USER_COUNT == 2:
            StartGameMultiplayer()


print("[SERVER] Server is starting.....")
start()
