import socket

# Laver ny socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Virker kun hvis server kører på egen computer, ellers skal der difeneres hvilken ipv4 adresse serveren kører på
hostname = socket.gethostname()
address = socket.gethostbyname(hostname)

print(address)
# Port skal matches med server port
port1 = 30000
port2 = 40000

# Sættes til IPv4 som serveren køres på
try:
    c.connect((address, port1))
except:
    c.connect((address, port2))

# Buffer size skal være 4096 eller derover ellers bliver alt data ikke sendt.
Message = c.recv(4096)

# Str skal decodes når de bliver modtaget
print(Message.decode('ascii'))

# Åbner output.txt i write mode for at slette content, derefter lukkes den
open("../output.txt", "w").close()

# Lukker socket connecetion
while True:
    Input = input('Say Something: ')
    c.send(str.encode(Input))
    Response = c.recv(1024)
    print(Response.decode('utf-8'))
