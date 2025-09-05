#!/usr/bin/env python3
#Taha Akyuz
#To Do List Program

#Importing libraries
import platform                                 #Checks operating system with platform.system
from os import system                           #Run operating system shell commands
from pathlib import Path                        #Gets user home directory



def checkFile():                                #Check if todo.txt already exists
    try:                                        #Try creating the file
        file = open("todo.txt", "x")
        print("No file found. Creating a new one...")              
    except FileExistsError:                     #If it already exixts, do nothing and continue running the program
        return


def readTasks():                                #Gets tasks from todo.txt
    with open("todo.txt", "r") as file:         #Open the file in read mode
        return [line.strip().split("; ") for line in file.readlines() if line.strip()]  #Return the tasks in a list
            


def addTask(title, description, priority):      #Accepts title, description, and priority as variables. Adds the task to todo.txt
    with open("todo.txt", "a") as file:         #Open the file in append mode
        file.write(f"{title}; {description}; {priority}\n") #Write the task to the file
    system(clrCmd)
    print(f"Task '{title}' added!")             #Print a message to the user that the task has been added


def rmTask():                                   #Remove a task from todo.txt
    tasks = readTasks()                         #Get the tasks from todo.txt
    if not tasks:                               #If the task list is empty, print a message and return
        print("No tasks to remove.")
        return

    print("Tasks:")                             #If there are tasks, enumerate them and print them to the user
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task[0]}")

    try:                                        #Ask the user to input the number that goes with the task they want to remove
        choice = int(input("\nWhich task would you like to remove? Or press enter to return to the main menu: ")) - 1
        if 0 <= choice < len(tasks):            #If the number is within the range of the task list, remove the task and print a message to the user
            removedTask = tasks.pop(choice)
            with open("todo.txt", "w") as file:
                for task in tasks:
                    file.write("; ".join(task) + "\n")
                system(clrCmd)
                print(f"Task '{removedTask[0]}' removed!")  #Print a message to the user that the task has been removed
        else:                                   #If the number is not within the range of the task list, print a message to the user and call the function again
            system(clrCmd)
            print("Invalid task number.")
            rmTask()
    except ValueError:                          #If the user doesn't input a number, print a message to the user and return them to the main() function
        system(clrCmd)
        main()


def taskLookup(searchTerm):                     #Search for a task in todo.txt
    with open("todo.txt", "r") as file:         #Open the file in read mode
        lines = file.readlines()
        for line in lines:                      #For each line in the file, check if the search term is in the line
            if line.find(searchTerm) != -1:
                print("Results:\n" + line)      #If the search term is in the line, print the line to the user
            else:
                print("No results found. Try a different search term.") #If no tasks are found, ask the user to try a different search term

def main():
    global clrCmd 
    osName = platform.system()                  #Get name of OS
    match osName:
        case "Windows":
            clrCmd = "cls"                      #If the OS is Windows, assign "cls" to the clrCmd variable
        case _: 
            clrCmd = "clear"                    #Otherwise, assign "clear" to the clrCmd variable
    system(clrCmd)
    while True:                                 #Start an infinite loop so the user can keep selecting menu options until they want to exit the program
        userAction = input("What do you need to do?\n\n1. Add a task\n2. Remove a task\n3. Search\n4. Exit\n\nSelect an option: ")
        match userAction:
            case "1":
                system(clrCmd)
                title = input("Enter the title of the task: ")  #Ask the user for the title, description, and priority of the task
                description = input("Enter the description of the task: ")
                priority = input("Enter the priority of the task: ")
                titleLower = title.lower()      #Assign the lowercased title, description, and priority to new variables
                descriptionLower = description.lower()
                priorityLower = priority.lower()
                addTask(titleLower, descriptionLower, priorityLower)   #Call the addTask function with the lowercased title, description, and priority as arguments
            case "2":
                system(clrCmd)
                rmTask()                        #Call the rmTask function
            case "3":
                searchTerm = input("Search for: ")
                system(clrCmd)
                taskLookup(searchTerm)
            case "4":
                exit()
            case _:                             #If an invalid option is selected, make fun of the user and ask them again
                system(clrCmd)
                print("That's not a valid option, silly.")


if __name__ == "__main__":
    checkFile()                                 #Check if todo.txt already exists, create it if it doesn't
    print("Welcome to your To Do List!")
    main()                                      #Initiate the main function