debug = True

print('Welcome to League of legends simulator')

UserInput = 0
while UserInput not in ['1', '2']:
    print("""
            1 - Battle against computer    
            2 - Battle against other player""")
    UserInput = input()
    if UserInput not in ['1', '2']:
        print('Enter a Valid input')


if UserInput == '1':
    print("Started gameSimulator")
    # gameSimulator.gameSimulator.game_start()

if UserInput == '2':
    print("Started work against other player")

if debug:
    print(UserInput)
