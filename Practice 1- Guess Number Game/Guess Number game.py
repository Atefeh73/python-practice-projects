#Guess random nuber game
#import Ranodm nummber generator module
import random
#consider a variable for storing the best score that doesn't have any value
bestScore= None
#Consider a variable for game loop
playAgain='yes'

#replay loop
while playAgain=='yes':

#Game Rules(range,range size,difficulty)  
  
    #1- Range: ask user to add min/max for the range
    minimum=int(input("What is the lowest number you want to consider for the range?" ))
    maximum=int(input('What is the biggest  number you want to consider for the range? '))
    
    #2-Range size: 
    rangeSize=maximum-minimum

    #3-Difficulty level:
    #What gane level do you perefer:
    difficulty= input('Choose the level of difficulty: hard/medium/easy ').lower()

    #fwer attempts, larger range size
    if difficulty=='hard':
    #less attempt
        if rangeSize<= 20:
            attempt=5
        elif rangeSize<= 50:
            attempt=5
        else:
            attempt=3              
        

    elif difficulty=='medium':


        if rangeSize<= 20:
            attempt=7
        elif rangeSize<= 50:
            attempt=6
        else:
            attempt=5     
    
    else:
        
        if rangeSize<= 20:
            attempt=10
        elif rangeSize<= 50:
            attempt=8
        else:
            attempt=7                          
            
    #use radndom module to generate number and store it in number variable
    number=random.randint(minimum,maximum)
    #for test purpose!
    print(number)


    #consider a variable to store the attempt time that it's limmited for user
    #attempt=7


    #consider a list to store all the guessed numbers as a history of user input to avoid repetative numbers
    guessedNumbers=set()


    #consider a variable to store used attempts!
    attemptUsed= 0

#Main Game!

    #consider a for loop to repeating the attempt to reach the considered attempt number
    for i in range(attempt):
        #Consider try statement for error-handling if the user entered non-int input for guessing
        try:
            #consider a varuiable to ask user for entering their numbers between min and max range and remind them they have only few left atttempt chanc!
            userInput=int(input(f'Guess a number between {minimum}  to {maximum}? attempt times: {attempt-i} '))


            #consider conditional statement to evaluate repitetive inputs and let the user now, then continue playing
            if userInput in guessedNumbers:
                    print('You already guessed that number!')
                    continue
            # consider a set method(add to the set) and let user continue playing without decreasing the attempt chance! take user input and add it to the list of guessed numbers
            guessedNumbers.add(userInput)
            attemptUsed+=1
            
            #conditional statement to evaluate user's input with random number
            if number==userInput:
                        print(f' 🎉 Congrats! You Wine in {attemptUsed} attempts!')
                        #Consider conditional staements if the best score reamin none or used attempts is lower than best score
                        if bestScore is None or attemptUsed<bestScore:
                                bestScore=attemptUsed
                                print("New best score!")


                        break
        
            elif number>userInput:
                        print('Too low!')
            else:
                        print('Too high!')  


        except ValueError:
                print('Please enter a valid number!')
                continue      
    else:
            print(f'You lost! The correct number is: {number}')          
    
    playAgain=input('play again?yes/no').lower()
