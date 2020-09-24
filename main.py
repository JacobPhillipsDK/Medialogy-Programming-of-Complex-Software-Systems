import logging
import numpy as np

print("Welcome to League of legends simulator!")

print("""1 - Start game""")
startGameInput = int(input())
if startGameInput == 1:
    print(""" 
        1 - Battle against computer    
        2 - Battle against other player
         """)
if startGameInput == 2:
    print("Currently Battle against other players wont work")
