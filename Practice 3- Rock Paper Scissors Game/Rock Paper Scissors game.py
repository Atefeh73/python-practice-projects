print('Rock Paper Scissors Game')

# import random module for generating random options
import random
# import getpass module for hiding player's choices in two-player mode
import getpass


# single player function:
def singlePlayerGame():

    print('You are playing with Computer!')

    # consider a variable to store user score:
    userScore=0
    # consider a variable to store user score:
    computerScore=0
    # consider a variable to store game rounds:
    roundGame=1
    
    # Internal loop to control the game round by 3 games: 
    for roundGame in range(3):
        
        # Ask user to enter their choice:
        userChoice=input('Choose on option: r,p,s?').lower()
        
        # Let computer generate a choice between given choices
        computerChoice=random.choice(['r','p','s'])
        print(f'Computer Choose:{computerChoice}')

        # Game evaluation; consider if statement to evaluate the results:
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

        # Results announsment for every round of the game(inside the internal loo):
        print(f'You: {userScore} | Computer: {computerScore}')
        print('---------------------------------')

    # Final result announsment after 3 rounds:
    if userScore>computerScore:
        print('You won the game!')
    elif computerScore>userScore:
        print('Computer won the game!')
    else:
        print('Overal Tie!')  

#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# two-player function:

def twoPlayer():
    print('Two player game!')

    # Consider 2 variable to store players scores
    player1Score=0
    player2Score=0

    # Internal loop to control the game round by 3 games: 
    for roundGame in range(3):
       
        # Ask both players to enter their Choices(neither of players can see each other choices):
        plyer1Choice=getpass.getpass(f'Hey {player1Name}! Please choose: r,p,s: ').lower()
        player2Choice=getpass.getpass(f'Hey {player2Name}! Please choose: r,p,s: ').lower()

        
        # Game evaluation; consider if statement to evaluate the results:
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
            

        # Results announsment for every round of the game(inside the internal loo):
        print(f'{player1Name}: {player1Score} | {player2Name}: {player2Score}')
        print('---------------------------')

    
        # Final result announsment after 3 rounds:
    if player1Score>player2Score:
        print(f'Congratulation! {player1Name} wins the game ')

    elif player2Score>player1Score:
        print(f'Congratulation! {player2Name} wins the game ')
    else:
        print('Overal tie!')    



# Main game loop:
# Consider a variable to store the reaction of user for replaying the game
playAgain='y'

# Keep playing while the user input is y
while playAgain=='y':

    # ask for game mode:
    gameMode=input('Choose the game mode: Single-player/ Two-Player: ').lower()

    if gameMode=='single':
        # call single player mode function:
        singlePlayerGame()
    elif gameMode=='two':
        # ask users to enter thier names:
        player1Name=input('Please enter player 1 name: ').lower()
        player2Name=input('Please enter player 2 name: ').lower()
        
        # call two player mode function:
        twoPlayer()
        
    else:
        print('Invalid game mode!')

    
    # Ask user in both game mode if they want to replay again or leave the game. 
    playAgain = input('Play again? Y/N: ').lower()
    if playAgain!='y':
            print('Thanks for playing!')
            break    

        
