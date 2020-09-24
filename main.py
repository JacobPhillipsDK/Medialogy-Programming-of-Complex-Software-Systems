import logging
import numpy as np

print("Welcome to League of legends simulator!")
startGameInput = 0
while startGameInput not in ['1']:
    print(""" 
            1 - Battle against computer    
            2 - Battle against other player""")
    startGameInput = (input())
    if startGameInput not in ['1', '2']:
        print("Currently Battle against other players wont work")

if startGameInput == [1]:
    print("Im gooood")
