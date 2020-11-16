import socket
from _thread import *

ThreadCount = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("socket created")
try:
    port = 30000
except:
    port = 40000

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(2)
print("socket is listening")

# Sletter data i output før et nyt spil startes
# open("output.txt", "w").close()

# Kører et spil på serveren
# startGame()

with open("../output.txt", "r") as File:
    data = File.read()
    first = File.read(1)


def ServerThread(connection):
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
    Client, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(ServerThread, (Client,))
    ThreadCount = ThreadCount + 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
