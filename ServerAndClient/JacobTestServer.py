import socket
import threading
import pickle

HEADERSIZE = 10
DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
SERVER = socket.gethostbyname(socket.gethostname())


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        # Siger længden af beskeden er 64 byte og skal formateres som utf-8
        msg_length = conn.recv(HEADERSIZE).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send(f"[SERVER] You have connected to {SERVER}".encode(FORMAT))
    conn.close()


# d = str("Hello")

def d():
    str = ("Hello, world")
    return str


def start():
    s.listen(2)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        thread = threading.Thread(target=handle_client, args=(clientsocket, address))

        thread.start()
        print(f"Connection from {address} has been established.")
        print(f"[ACTIVE CONNECTIONS]   {threading.active_count() - 1}")

        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
        print(msg)
        clientsocket.send(msg)


print("[SERVER] Server is starting.....")
start()
