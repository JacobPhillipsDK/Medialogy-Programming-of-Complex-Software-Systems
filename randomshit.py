list = [6,4,8,1,3,5]
players1 = []
players1.append(GS.PlayerRole("Kristian", 8, 8, 9))
players1.append(GS.PlayerRole("Jacob", 2, 3, 4))
players1.append(GS.PlayerRole("Nicklas", 6, 8, 6))
players1.append(GS.PlayerRole("Mikkel", 7, 9, 5))
players1.append(GS.PlayerRole("Lukas", 6, 8, 5))

players2 = []
players2.append(GS.PlayerRole("Poul",5,7,6))
players2.append(GS.PlayerRole("Frank",7,8,9))
players2.append(GS.PlayerRole("Erik",5,8,9))
players2.append(GS.PlayerRole("Lars",10,8,9))
players2.append(GS.PlayerRole("george",6,2,9))


for i in range(len(players1)-1,0,-1):
    for j in range(i):
        if list[j]>list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]


print(list)
print("hej")