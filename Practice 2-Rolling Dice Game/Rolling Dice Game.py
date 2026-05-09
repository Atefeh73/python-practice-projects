print('lets play a game!')
#adding random number generator
import random
#Define a loop to stop the game when responce is n!
while True:
#define a variable with int type to ask and store user iput for game starting    
    responce=input('Would you like to play a game?').lower()
#Define condition to ask number of the time the user want to play!    
    if responce=='y':
        roll=int(input("How many time you want to play?"))
#Use for loop to print the random generated numbers to reach the entered numbers of rolling!
        for i in range(roll):
            dice1=random.randint(1,6)
            dice2=random.randint(1,6)
            print(f'Roll {i+1}:{dice1},{dice2}')
# Why i+1? because in programming, counting of the numbers starts from 0           
            print(f'You rolled about: {i+1} times!')
    elif responce=='n':
        print('Thanks for playing!')
        break
    else:
        print('invalid responce!')
