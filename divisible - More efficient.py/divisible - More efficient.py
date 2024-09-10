#!/usr/bin/python

def main():
    numberA = int(input("Enter your first number.\n"))
    numberB = int(input("Enter your second number.\n"))
    isDivisible(numberA, numberB)
    askAgain = input("Do you want to go again? (y/n)\n")
    if askAgain == "y":
        main()
    else:
        print("Bye.")
    
def isDivisible(x, y):
    userInputs = "{} and {}".format(x, y)
    if x < y or x == y:
        print("Your first number should be greater than your second number!\nStarting over!\n")
        main()
    else:
        answer = x + 1
        while answer % y:
            answer += 1
        print("The next number greater than {} and is divisible by {} is {}".format(userInputs, y, answer))

if __name__ == "__main__":
    main()