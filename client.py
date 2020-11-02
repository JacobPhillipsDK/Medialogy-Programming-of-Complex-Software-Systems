import socket

#Laver ny socket
s = socket.socket()

#Port skal matches med server port
port = 40000

#Sættes til IPv4 som serveren køres på
s.connect(('192.168.1.3', port))

#Buffer size skal være 4096 eller derover ellers bliver alt data ikke sendt.
Message = s.recv(4096)

#Str skal decodes når de bliver modtaget
print(Message.decode('ascii'))

#Åbner output.txt i write mode for at slette content, derefter lukkes den
open("output.txt", "w").close()

#Lukker socket connecetion
s.close()