#/usr/bin/env python3

#Taha Akyuz
#Information Technology
#IT Dictionary

##Importing Libraries##
import json #Library to work with JSON files
import time #Library used for date/time information
import platform #Used to get OS name
import subprocess #Used to run powershell commands
from os import system #Used to run commands from the Python interpreter

userPlatform = platform.system()

if userPlatform == "Windows": #If the OS is Windows...
    clearCommand = "cls" #...set the clear command to "cls"
else: #Otherwise...
    clearCommand = "clear" #...set it to "clear"

try:
    loaded = open("cspterms.json", "r") #Open the dictionary JSON file
except FileNotFoundError: #If the dictionary file doesn't exist
    data = {}
    with open("cspterms.json", "w") as f: #Create the file...
        json.dump(data, f, indent=4) #...and put the curly brackets in there
    loaded = open("cspterms.json", "r") #Open the dictionary JSON file
    
    
data = loaded.read() #Load the JSON data into memory
loaded.close() #Close the dictionary file

convertedData = json.loads(data) #Convert data from string type to dictionary data type

def newTerm():
    system(clearCommand) #Clear the screen
    termName = input("Enter a new term or change an existing one: ") #Ask the user for the term and assign it to a variable
    termDef = input("Define {}:\n".format(termName)) #Ask the user for the definition and assign it to a variable
    convertedData[termName] = termDef #Add the term to the dictionary along with its definition. It is only in memory and not saved to the JSON file at this point, that happens next.
    writeToFile() #Write the new term and its definition to the JSON file


def showAllTerms():
    system(clearCommand) #Clear the screen
    for key in convertedData: #For every term in the dictionary...
        print(key.upper(), ": ", convertedData[key]) #...print the term and its definition
    input("Press Enter to return to the main menu...") #Pause the program so the user can look at the output, wait for an input to continue

def viewTerm():
    system(clearCommand) #Clear the screen
    for key in convertedData:
        print(key) #Print every term in the dictionary
    selectedTerm = input("Enter the term you want to view: ") #Ask the user which term they want to view
    system(clearCommand) #Clear the screen
    try:
        print("The definition of {} is:\n{}".format(selectedTerm, convertedData[selectedTerm])) #If the term exists, print the definition
    except KeyError:
        system(clearCommand) #Clear the screen
        print("The term \"{}\" is not found in your dictionary. Make sure the term exists and you've spelled it correctly.\n".format(selectedTerm)) #If the term doesn't exist, tell the user

def removeTerm():
    system(clearCommand) #Clear the screen
    for key in convertedData:
        print(key) #Print every term in the dictionary
    termToRemove = input("Enter the term you would like to remove: ") #Ask the user which term they want to remove
    system(clearCommand) #Clear the screen 
    try:
        del convertedData[termToRemove] #Delete the term from the dictionary
        print("{} was removed from your dictionary.".format(termToRemove)) #Tell the user the term was removed successfully
        writeToFile() #Write changes to the JSON file
    except KeyError:
        system(clearCommand) #Clear the screen
        print("The term \"{}\" is not found in your dictionary. Make sure the term exists and you've spelled it correctly.\n".format(termToRemove)) #If the term doesn't exist, tell the user

def backupDictionary():
    backupFileName = "{}-cspterms".format(time.strftime("%Y%m%d-%H%M%S")) #Assign the format of the backup file to a variable
    if userPlatform == "Windows":
        subprocess.run(["powershell", "Copy-Item", "cspterms.json", "{}.json".format(backupFileName)], check=True) #Run the copy command through powershell since cmd doesn't support network paths
    else:
        system("cp cspterms.json {}.json".format(backupFileName)) #Create the backup
        system("ls -lth {}.json".format(backupFileName)) #Get file details and show it to the user
    print("Done.")
    input("Press enter to return to the main menu...") #Pause the program so the user can look at the output, wait for an input to continue

def writeToFile():
    writeData = json.dumps(convertedData, indent = 4) #Put the data to be written in the correct format for a JSON file
    toFile = open("cspterms.json" , "w") #Open the dictionary JSON file
    toFile.write(writeData) #Write the changes to the JSON file
    toFile.close #Close the file
    return

def main():
    while True: #Infinite loop so the menu is always shown to the user
        userChoice = input("What would you like to do?\n1. Enter a new term or change an incorrect one\n2. View entire dictionary\n3. View a specific term\n4. Delete a term\n5. Create a backup...\n6. Exit\nInput: ")
        if userChoice == "1":
            newTerm()
        elif userChoice == "2":
            showAllTerms()
        elif userChoice == "3":
            viewTerm()
        elif userChoice == "4":
            removeTerm()
        elif userChoice == "5":
            backupDictionary()
        elif userChoice == "6":
            print("Goodbye!")
            quit()

if __name__ == "__main__":
    main()