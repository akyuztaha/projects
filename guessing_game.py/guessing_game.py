#!/usr/bin/python
#Taha Akyuz
#Random Generator

####Defining Variables####
totalMatches = 0
totalWins = 0

####Importing Libs####
from random import randint
from IPython.display import clear_output

# Define function randomizer which will generate a random number between 0 and 1000, then assign it to variable randomNum
def randomizer():
    global totalMatches
    global totalWins
    
    randomNum = randint(0,1000)
    #print(randomNum)
    for guesses in range(1,11): # Keep track of guesses, starting from 1 and going up to 11
        print("Attemp number {}".format(guesses)) # Print the attempt number
        myGuess = int(input("What is your guess?")) # Ask the user for ther guess
        
        if guesses == 10 and myGuess != randomNum: # If the user uses all their guesses and doesn't find the answer
            print("Sorry, you lose!\nThe number you were looking for was {}".format(randomNum))
            totalMatches += 1
            exit()
            break
            
        if myGuess == randomNum:
            print("You win! You guessed {}".format(myGuess)) # Output for when user guesses the correct number
            totalMatches += 1
            totalWins += 1
            exit()
            break
            
        if myGuess < randomNum:
            print("The number is higher than {}".format(myGuess)) # Tell user answer is higher than their guess
            
        if myGuess > randomNum:
            print("The number is lower than {}".format(myGuess)) # Tell user answer is lower than their guess
            
    
# Define function exit which whill exit the program
def exit():
    exitQuestion = input("One more time? (yes/no) or (y/n) ==> ") # Assign the user input to var exitQuestion
    
    if exitQuestion == "y": # If exitQuestion is "y", run func randomizer
        clear_output()
        randomizer()
        
    elif exitQuestion == "yes": # If exitQuestion is "yes", run func randomizer
        clear_output()
        randomizer()
        
    elif exitQuestion == "n": # If exitQuestion is "n", print "Bye" and exit
        clear_output()
        print()
        print("You won {} out of {} games".format(totalWins, totalMatches))
        print("Bye")
    
    elif exitQuestion == "no": # If exitQuestion is "no", print "Bye" and exit
        clear_output()
        print()
        print("You won {} out of {} games".format(totalWins, totalMatches))
        print("Bye")
        
    else:
        clear_output()
        print("Please input 'y', 'n', 'yes', or 'no'.") # If value of exitQuestion is anything else, run func exit to prompt user again
        exit()
    
# Greet the user, generate and print the amount of numbers the user asks for.
if __name__ == "__main__":
    print("Welcome to the Random Number Generator!")
    print()
    randomizer()