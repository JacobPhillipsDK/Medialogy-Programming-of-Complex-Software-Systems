import socket
import threading
from main2 import *
global USER_COUNT
global players1
global players2

# 64 byte
HEADERSIZE = 64
HEADER = 64
# Port
PORT = 4050
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


def readStringExecutive(String):
    a = str(String)
    # Was used for debugging purposes
    # print(a)
    exec(a)


def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words


def GemSata(InputData):
    file2Write = open("Filer der ikke bliver brugt mere/DataSend.txt", "a")
    file2Write.write(f"{InputData}")
    file2Write.close()
    return None


players3 = []
players4 = []


def StartGameMultiplayer():
    print("I work")
    Player1 = GS.Team("Player 1", players3)
    Player2 = GS.Team("PLayer 2", players4)
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
            readStringExecution(msg)
            if len(players3) == 5 and len(players4) == 5:
                print("Starting gameSimulator")
                StartGameMultiplayer()
            conn.send(f"[SERVER] You have connected to {SERVER}".encode(FORMAT))
    conn.close()


def readStringExecution(String):
    exec(f'{String}')


# Starer socket server
# Lytter efter forbindelse anmodninger
def start():
    server.listen(2)
    open("output.txt", "w").close()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]   {threading.active_count() - 1}")
        USER_COUNT = int((threading.active_count() - 1))
        print(f"[ACTIVE USER_COUNT:]  {USER_COUNT}")



print("[SERVER] Server is starting.....")
start()
