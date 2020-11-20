import socket
from _thread import *
import time

# Her siger vi at threadcount er 0
ThreadCount = 0

# Printer de sockets der er blevet lavet.
print("socket created")
port = 4050


# Henter local maksine navn
myHostName = socket.gethostname()
local_ip = socket.gethostbyname(myHostName)
print("Name of the localhost is {}".format("Name of computer  : " + " " + myHostName + " IP :  " + local_ip))

# Lavet et socket objekt
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((myHostName, port))
print("socket binded to %s" % (port))

# Her tager vi i mod op til 2 forbindelser på en gang
serversocket.listen(2)
print("socket is listening for request......")


# Sletter data i output før et nyt spil startes
# open("213213213.txt", "w").close()

# Kører et spil på serveren
# startGame()

with open("../output.txt", "r") as File:
    data = File.read()
    first = File.read(1)


def ClientThread(connection):
    connection.send(str.encode('You are connected, type to recieve data'))
    while True:
        data2 = connection.recv(2048)
        error = 'Error: There is no data'
        if not data2:
            break
        if not first:
            connection.send(str.encode(error))

        connection.send(data.encode('ascii'))


while True:
    Client, addr = serversocket.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(ClientThread, (Client,))
    ThreadCount = ThreadCount + 1

    print('Thread Number: ' + str(ThreadCount))
    serversocket.close()
