def decToHex():
    decNumber = int(input("What number do you want to convert to hexadecimal? "))
    hexval = hex(decNumber).lstrip("0x")
    print("Decimal: ", decNumber, "/ Hexadecimal: ", hexval)
    againAns = input("What now?\n1. Again\n2. Exit to main menu\nType in the corresonding number ==> ")
    if againAns == "1":
        decToHex()
    elif againAns == "2":
        menu()

def hexToDec():
    hexNumber = input("What hexadecimal value do you want to convert to decimal? ")
    decval = int(hexNumber, 16)
    print("Decimal: ", decval, "/ Hexadecimal: ", hexNumber)
    againAns = input("What now?\n1. Again\n2. Exit to main menu\nType in the corresonding number ==> ")
    if againAns == "1":
        hexToDec()
    elif againAns == "2":
        menu()

    
def menu():
    request = input("What do you want to do?\n1. Decimal to Hexadecimal\n2. Hexadecimal to Decimal\nType in the corresponding number ==> ")
    if request == "1":
        decToHex()

    elif request == "2":
        hexToDec()
        
menu()
