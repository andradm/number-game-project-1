import random


def start_game():
    
    
    #Print a welcome message
    
    print("------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------", "\n")
    
    #Store a random number as the answer/solution.
    answer = random.randint(1,10)
    tries = 1
    
    
    #Continuously prompt the player for a guess in a "while" loop
	   
    while True:
        try:
            guess = int(input("Please, pick a number between 1 and 10: "))
            if guess > 10 or guess < 1:
                print("Ops! That's not valid. Please pick a number between 1 and 10.")
                continue
            #If guess is higher than answer, print "It's higher!"  
            elif guess < answer:
                print("It's higher!")
                tries += 1
                continue
            #If guess is lower than answer, print "It's lower!"  
            elif guess > answer:
                print("It's lower!")
                tries += 1
                continue
            #If guess is correct, print "Got it" and a message that says how many attempts it took the player to guess it. Finalize with a sentence that indicates the game ended.End the loop)
            elif guess == answer:
                print("Got it! It took you {} attempt(s).".format(tries))
                print("Thanks for playing!")
                break
        except ValueError:
            print("Ops! That's not valid. Please pick a number between 1 and 10.")
            continue
#call function start_game()        
start_game()     