##1 Importing library module, random
# -*- coding: cp1252 -*-
import random
 
#let's pick a random number between 0 and 99
#the easiest way is to use the random module's funtion randint
number = random.randint(0,100)
print("Program picked a number:",number)

##2 Example: Ending program, sys-module
# -*- coding: cp1252 -*-
import sys
 
startprice = int(input("Please input the price: "))
if startprice < 0:
    print("Please, no negative numbers.")
    sys.exit(0)
else:
    tax = int(input("Please insert the VAT % (0-100): "))
if tax < 0:
    print("VAT cannot be less than 0.")
    sys.exit(0)
print("Final price is",startprice*(tax/100)+startprice)

##4 Example1: Mathematical functions, math-module
# -*- coding: cp1252 -*-
# import math

# side_1 = 1.5
# side_2 = 3.5

# print(math.sin(1.5 / 3.5))
# print(math.pi)

##4 Example2: Picking lottery numbers
# -*- coding: cp1252 -*-
import random  
numbers = []
#picks 7 random numbers from 1 to 39
while True:
    if len(numbers) == 7:
        break
    pick = random.randint(1,39)
    if pick not in numbers:
       numbers.append(pick)

numbers.sort()
print("The program picked the following numbers:")

for i in numbers:
    print(i, end = ' ')



##4 Example3: Importing individual function
# -*- coding: cp1252 -*-
from random import randint
import sys

def numbergame():
    number = randint(0,100)
    while True:
         
        guess = int(input("Give a number between 0-100: "))
        if guess < 0:
            print("Bad guess!")
            print("Program is terminated.")
            sys.exit(0)
        if guess == number:
            print("You guessed correctly!")
            break
        elif guess < number:
            print("The number is larger than that.")
        else:
            print("The number is smaller than that.")

if __name__ == "__main__":
    numbergame()


##6 Example: Importing own modules
# -*- coding: cp1252 -*-
import mymodule
  
def main():
    salary = int(input("Give monthly salary: "))
    tax = int(input("Give tax percentage (0-100): "))
    sum = mymodule.taxcalculator(salary,tax)

    print("You'll get", sum,"euros.")

if __name__ == "__main__":
    main()


##7
import mymodule
print(mymodule.fixedvalue)
mymodule.printout()
