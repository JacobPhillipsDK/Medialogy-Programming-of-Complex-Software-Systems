import socket
from main2 import startGame

s = socket.socket()
print("socket created")
port = 40000

s.bind(('', port))
print ("socket binded to %s" %(port) )
s.listen(5)
print("socket is listening")
startGame()

with open ("output.txt", "r") as File:
    data=File.read()
while True:
    c, addr = s.accept()
    print('connection from', addr)
    #Str skal encodes når de sendes

    c.send(data.encode('ascii'))
    c.close()



