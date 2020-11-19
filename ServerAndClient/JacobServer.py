import socket
from main2 import *
import threading
import pickle
from GameMechanics import gameSimulator as GS

global playerNames
global USER_COUNT

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
    file2Write = open("DataGem.txt", "a")
    file2Write.write(f"{InputData}")
    file2Write.close()
    return None


players1 = []
players2 = []

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
    conn.close()


def PickleHandler():
    while True:
        full_msg = b''
        new_msg = True
        while True:
            msg = server.recv(16)
            if new_msg:
                # print("new msg len:",msg[:HEADERSIZE])
                msglen = int(msg[:HEADERSIZE])
                new_msg = False
            # print(f"full message length: {msglen}")
            full_msg += msg
            # print(len(full_msg))
            if len(full_msg) - HEADERSIZE == msglen:
                print("I can received message from [SERVER]")
                print(full_msg[HEADERSIZE:])
                print(pickle.loads(full_msg[HEADERSIZE:]))
                GemSata(pickle.loads(full_msg[HEADERSIZE:]))
                new_msg = True
                full_msg = b""


# Starer socket server
# Lytter efter forbindelse anmodninger
def start():
    server.listen(2)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thead_pickle = threading.Thread(target=PickleHandler, args=(conn,addr))
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thead_pickle.start()
        thread.start()
        print(f"[ACTIVE CONNECTIONS]   {threading.active_count() - 1}")
        USER_COUNT = int((threading.active_count() - 1))
        print(f"[ACTIVE USER_COUNT:]  {USER_COUNT}")
        #PickleHandler()
        # d = readFile("DataSend.txt")
        # msg = pickle.dumps(d)
        # msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
        # print(msg)


print("[SERVER] Server is starting.....")
start()
