import random

def guessing():
    #initialize a random number between 1~100
    rand_num = random.randint(1, 100)
    
    #initizalize how many guesses the player has made
    attempts = 0
    
    #initialize the max number of guesses the player can make
    max_attempts = 10
    
    #initialize the player guess
    guess = int(input("Guess a number between 1 and 100 \n"))
    
    #initialize lower and upper bound of guess
    lower = 1
    upper = 100
    
    while True:       
        
        #check if the input is the number
        if guess < rand_num:
            #player's guess is too low
            print("Your guess is too low, guess higher")
            
            #set the guess as lower bound
            lower = guess
            
            #new comment telling player to guess again using their new number
            guess = int(input(f"Guess a number between {lower} and {upper} \n"))
            
            #increase attempt counter   
            attempts += 1
            
        elif guess > rand_num:
            #player's guess is too high
            print("Your guess is too high, guess lower")
            
            #set ghe guess a upper bound
            upper = guess
            
            #new comment telling player to guess again using their new number
            guess = int(input(f"Guess a number between {lower} and {upper} \n"))
            
            #increase attempt counter
            attempts += 1       
        else: #player has guessed correctly
            print("You have guessed the number" , rand_num)
            break
        
        #comment telling the player how many attempts they have made and how many attempts they have left
        print("You have made" , attempts , "attempts. You have " , max_attempts - attempts , "attempts left \n")
        
        
        #check if max attempts have been hit
        if attempts == max_attempts:
            print("You have used all" , attempts , "attempts. The number was", rand_num)
            break
        
        
guessing()