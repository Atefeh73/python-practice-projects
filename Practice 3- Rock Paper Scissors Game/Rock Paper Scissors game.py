print('Game')
import random 
import getpass
# single player function:

def singlePlayerGame():

    print('You are playing with Computer!')


    userScore=0
    computerScore=0
    roundGame=1
    

    for roundGame in range(3):
        userChoice=input('Choose on option: r,p,s?').lower()
        computerChoice=random.choice(['r','p','s'])
        print(f'Computer Choose:{computerChoice}')

        if computerChoice==userChoice:
            print('Game is tie!')
        elif (computerChoice=='r' and userChoice=='p'
            or  computerChoice=='p'  and userChoice=='s'
            or  computerChoice=='s'  and userChoice=='r'):

            print('You win this round')
            userScore+=1
        else:
            print('Computer wins!')
            computerScore+=1 


        print(f'You: {userScore} | Computer: {computerScore}')
        print('---------------------------------')


    if userScore>computerScore:
        print('You won the game!')
    elif computerScore>userScore:
        print('Computer won the game!')
    else:
        print('Overal Tie!')        

#two-player function:

def twoPlayer():
    print('Two player game!')

    player1Score=0
    player2Score=0
    
    #player1Name=input('Please enter player 1 name: ').lower()
    #player2Name=input('Please enter player 2 name: ').lower()
    for roundGame in range(3):
        #player1Name=input('Please enter player 1 name: ').lower()
        #player2Name=input('Please enter player 2 name: ').lower()

        plyer1Choice=getpass.getpass(f'Hey {player1Name}! Please choose: r,p,s: ').lower()
        player2Choice=getpass.getpass(f'Hey {player2Name}! Please choose: r,p,s: ').lower()
        

        if plyer1Choice==player2Choice:
            print(f'It is tie! {player1Name} choose: {plyer1Choice} & {player2Name} choose: {player2Choice}')
        elif (
                plyer1Choice=='r' and player2Choice=='s' or
                plyer1Choice=='s' and player2Choice=='p' or 
                plyer1Choice=='p' and player2Choice=='r'
              ):
                print(f'{player1Name} wins this round!{player1Name} choose: {plyer1Choice} & {player2Name} choose: {player2Choice}')
                player1Score+=1

        else:
            print(f'{player2Name} wins this round! {player1Name} choose: {plyer1Choice} & {player2Name} choose: {player2Choice}')
            player2Score+=1


        print(f'{player1Name}: {player1Score} | {player2Name}: {player2Score}')
        print('---------------------------')

    if player1Score>player2Score:
        print(f'Congratulation! {player1Name} wins the game ')

    elif player2Score>player1Score:
        print(f'Congratulation! {player2Name} wins the game ')
    else:
        print('Overal tie!')    



#Main game loop:

playAgain='y'

while playAgain=='y':

    #ask for game mode:
    gameMode=input('Choose the game mode: Single-player/ Two-Player: ').lower()

    if gameMode=='single':
        singlePlayerGame()
    elif gameMode=='two':
        player1Name=input('Please enter player 1 name: ').lower()
        player2Name=input('Please enter player 2 name: ').lower()
        twoPlayer()
    else:
        print('Invalid game mode!')

    playAgain = input('Play again? Y/N: ').lower()
    if playAgain=='n':
            print('Thanks for playing!')
            break    

        