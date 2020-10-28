import socket

s = socket.socket()

port = 40000

s.connect(('192.168.1.103', port))

Message = s.recv(4096)
#Str skal decodes når de bliver modtaget
print(Message.decode('ascii'))

open("output.txt", "w").close()

s.close()