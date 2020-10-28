import socket

s = socket.socket()
print("socket created")
port = 40000

s.bind(('', port))
print ("socket binded to %s" %(port) )
s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('connection from', addr)
    msg = 'You are connected'
    #Str skal encodes når de sendes
    c.send(msg.encode('ascii'))
    c.close()