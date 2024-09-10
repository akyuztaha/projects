#!/bin/bash/python
#Taha Akyuz

from time import sleep
from datetime import datetime

def main():
    global now
    now = datetime.now()
    print("Welcome to payroll.py!")
    sleep(1)
    employeeName()

def employeeName():
    global employeeFirstName
    employeeFirstName = input("Who is this paystub for?\nEmployee First Name: ")
    global employeeLastName
    employeeLastName = input("Last Name: ")
    global employeeFullName
    employeeFullName = employeeLastName + ", " + employeeFirstName
    askNameCorrect = input("{}. Is that correct?\nPlease enter 'y' or 'n': ".format(employeeFullName))
    if askNameCorrect == "y":
        print("Got it.")
        employeePay()
    else:
        print("No problem. Let's try again...")
        sleep(0.75)
        employeeName()

def employeePay():
    print("\nNow for the pay.")
    global payRate
    payRate = float(input("What is {}'s hourly rate? ".format(employeeFirstName)))
    global hoursWorked
    hoursWorked = float(input("How many hours did {} work? ".format(employeeFirstName)))
    global overtimeHours
    global grossPay
    if hoursWorked <= 40:
        grossPay = payRate * hoursWorked
        overtimeHours = 0
    else:
        overtimeHours = hoursWorked - 40
        grossPay = (payRate * 40) + (overtimeHours * (payRate * 1.5))
    employeeDeductions()
    
def employeeDeductions():
    print("\nNow for the deductibles.")
    global fedTax
    fedTax = 0.12
    print("Federal tax is 12%.")
    global stateTax
    stateTax = 0.05
    print("State tax is 5%")
    global ssTax
    ssTax = 0.062
    print("Social Security is 6.2%.")
    global insuranceFee
    insuranceFee = 60
    print("Insurance is $60")
    input("Hit any key to continue.")
    global fedTaxDeductions
    fedTaxDeductions = grossPay * 0.12
    print("\nTotals:")
    print("Federal tax deduction: {:.2f}".format(fedTaxDeductions))
    global stateTaxDeductions
    stateTaxDeductions = grossPay * 0.05
    print("State tax deduction: {:.2f}".format(stateTaxDeductions))
    global ssTaxDeductions
    ssTaxDeductions = grossPay * 0.062
    print("Social Security deduction: {:.2f}".format(ssTaxDeductions))
    print("Insurance deduction: {:.2f}".format(insuranceFee))
    global totalDeductions
    totalDeductions = fedTaxDeductions + stateTaxDeductions + ssTaxDeductions + insuranceFee
    print("Total deductions: {:.2f}".format(totalDeductions))
    print("\nGross pay: {:.2f}".format(grossPay))
    global netPay
    netPay = grossPay - totalDeductions
    print("Net pay: {:.2f}".format(netPay))
    askDedCorrect = input("Do these look correct (y/n)? ")
    if askDedCorrect == "y":
        print("Ok. Moving on.")
        results()
    else:
        print("Ok. Let's try again...")
        employeePay()

def results():
    for loop in range(10):
        print()
    print("Ok. Here's what I've gathered.\n")
    print("Paystub for: {}".format(employeeFullName))
    print("\nHours:")
    if overtimeHours == 0:
        print("Total hours: {:.1f}\nRegular hours: {:.1f}\nOvertime hours: N/A".format(hoursWorked, hoursWorked))
    else:
        print("Total hours: {:.1f}\nRegular hours: {:.1f}\nOvertime hours: {:.1f}".format(hoursWorked, hoursWorked - overtimeHours, overtimeHours))
    print("\nDeductions:")
    print("Federal tax rate: 12%\nState tax rate: 5%\nSocial Security rate: 6.2%\nInsurance: $60")
    print("\nFederal tax deducted: {:.2f}\nState tax deducted: {:.2f}\nSocial Security deducted: {:.2f}\nInsurance fee: $60\n\nTotal deductions: {:.2f}".format(fedTaxDeductions, stateTaxDeductions, ssTaxDeductions, totalDeductions))
    print("\nYour pay:\nGross pay: {:.2f}\nNet pay: {:.2f}".format(grossPay, netPay))
    askGoAgain = input("Would you like to start over for another employee (y/n)? ")
    if askGoAgain == "y":
        writeToFile()
        main()
    else:
        writeToFile()
        print("Have a nice day!")
    

def writeToFile():
    payStub = open("{}-{}-paystub.txt".format(employeeLastName, employeeFirstName), "w+")
    payStub.write("Paystub for: {}\n".format(employeeFullName))
    payStub.write(now.strftime("File created: %m/%d/%Y %H:%M:%S\n"))
    payStub.write("\nHours:\n")
    if overtimeHours == 0:
        payStub.write("Total hours: {:.1f}\nRegular hours: {:.1f}\nOvertime hours: N/A".format(hoursWorked, hoursWorked))
    else:
        payStub.write("Total hours: {:.1f}\nRegular hours: {:.1f}\nOvertime hours: {:.1f}".format(hoursWorked, hoursWorked - overtimeHours, overtimeHours))
    payStub.write("\n\nDeductions:")
    payStub.write("\nFederal tax rate: 12%\nState tax rate: 5%\nSocial Security rate: 6.2%\nInsurance: $60\n")
    payStub.write("\nFederal tax deducted: {:.2f}\nState tax deducted: {:.2f}\nSocial Security deducted: {:.2f}\nInsurance fee: $60\nTotal deductions: {:.2f}\n".format(fedTaxDeductions, stateTaxDeductions, ssTaxDeductions, totalDeductions))
    payStub.write("\n\nYour pay:\nGross pay: {:.2f}\nNet pay: {:.2f}".format(grossPay, netPay))




if __name__ == "__main__":
    main()