import socket

#Laver ny socket
c = socket.socket()

hostname = socket.gethostname()
address = socket.gethostbyname(hostname)

#Port skal matches med server port
port = 40001

#Sættes til IPv4 som serveren køres på
c.connect((address, port))

#Buffer size skal være 4096 eller derover ellers bliver alt data ikke sendt.
Message = c.recv(4096)

#Str skal decodes når de bliver modtaget
print(Message.decode('ascii'))

#Åbner output.txt i write mode for at slette content, derefter lukkes den
open("output.txt", "w").close()

#Lukker socket connecetion
while True:
    Input = input('Say Something: ')
    c.send(str.encode(Input))
    Response = c.recv(1024)
    print(Response.decode('utf-8'))