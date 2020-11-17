import socket
import pickle
import threading

HEADERSIZE = 10
FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = socket.gethostbyname(socket.gethostname())

USER_ID = "PLayer 2"

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADERSIZE - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))



def RecvDaty():
    while True:
        full_msg = b''
        new_msg = True
        while True:
            msg = client.recv(16)
            if new_msg:
                print("new msg len:", msg[:HEADERSIZE])
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            print(f"full message length: {msglen}")

            full_msg += msg

            print(len(full_msg))

            if len(full_msg) - HEADERSIZE == msglen:
                print("full msg recvd")
                print(full_msg[HEADERSIZE:])
                print(pickle.loads(full_msg[HEADERSIZE:]))
                p = pickle.loads(full_msg[HEADERSIZE:])
                print(p)
                new_msg = True
                full_msg = b""

def start():
    client.connect((socket.gethostname(), 1243))
    send_msg(f" Username: {USER_ID} have connected to the server")
    thread = threading.Thread(target=RecvDaty)
    thread.start()
    print(f"[ACTIVE Threads] {threading.active_count() - 1}")
start()