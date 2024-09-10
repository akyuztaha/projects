#Taha Akyuz
#This program uses an algorithm to find the date Easter will be for any given year.

#1. Let y be the year (such as 1800 or 2001).
y = int(input("What is the year?"))

#2. Divide y by 19 and call the remainder a. Ignore the quotient.
a = y % 19

#3. Divide y by 100 to get a quotient b and a remainder c.
b = y // 100
c = y % 100

#4. Divide b by 4 to get a quotient d and a remainder e
d = b // 4
e = b % 4

#5. . Divide 8 times b + 13 by 25 to get a quotient g. Ignore the remainder.
stepFive = 8 * b + 13
g = stepFive // 25

#6. Divide 19 a + b-d-g + 15 by 30 to get a remainder h. Ignore the quotient.
stepSix = 19 * a + b - d - g + 15
h = stepSix % 30

#7. Divide c by 4 to get a quotient j and a remainder k.
j = c // 4
k = c % 4

#8. Divide a + 11 h by 319 to get a quotient m. Ignore the remainder.
stepEight = a + 11 * h
m = stepEight // 319

#9. Divide 2 e + 2*j-k-h + m + 32 by 7 to get a remainder r. Ignore the quotient.
stepNine = 2 * e + 2 * j - k - h + m + 32
r = stepNine % 7

#10. Divide h-m+r+ 90 by 25 to get a quotient n. Ignore the remainder.
stepTen = h - m + r + 90
n = stepTen // 25

#11. Divide h-m+r+n + 19 by 32 to get a remainder p. Ignore the quotient.
stepEleven = h - m + r + n + 19
p = stepEleven % 32

#12. create a list with the months that will be printed
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#13. take the n variable, and subtract 3 so as to choose the month in the list
actualMonth = months[n-1]

#14. Print out a formated print statement with placeholders for the variable y, actualMonth, and p
print()
print("In the year {}, Easter falls on {} {}.".format(y, actualMonth, p))
