import socket

s = socket.socket()

port = 40000

s.connect(('192.168.1.3', port))

Message = s.recv(1024)
#Str skal decodes når de bliver modtaget
print(Message.decode('ascii'))

s.close()