##2 Example: Creating a function

# # -*- coding: cp1252 -*-
# #Lets make a new function
# def hellofunction():
#     print("This print is from the function!")
# print("This print is from main code!")

# #Lets call the function
# hellofunction()
# print("Again, the main code butting in!")
# #Lets call the function again.
# hellofunction()


##3
# def Comparison(number_1, number_2):
#     """This function takes two integers."""

#     if number_1 == number_2:
#         print("The numbers are equal.")
#     elif number_1 > number_2:
#         print("The first number is larger.")
#     else:
#         print("The second number is larger.") 
# value1 = 10
# value2 = 12
# Comparison(value1, value2)
# Comparison(5,5)
# Comparison(value1, 0)


##4
# -*- coding: cp1252 -*-

# #Let's define a subfunction
# def printerfunction(word1,word2):
#     print("We got parameters",word1,"and",word2)

# #This is the main function
# def main():
#     string_1 = "Blues record"
#     string_2 = "Artichoke"

#     #Lets call the subfunction here
#     printerfunction(string_1, string_2)

# #This code tells the interpreter the name
# #of the main function which starts the program.
    
# if __name__ == "__main__":
#     main()


##6
# def divider(number1,number2):
#     if number2 == 0:
#         return False
#     else:
#         result = number1/number2
#         return result

# results = divider(100,0)
# print(results)
# results = divider(100, 20)
# print(results)


##7
###7.1
# def getlength(testme):
#     if len(testme) < 42:
#         return 0
#     else:
#         return 1

# result = getlength("ohgodwhydoesthisstringhavetobesolongicanteverrememberthis")
# if result == True:
#     print("This string is long enough.")
# else:
#     print("This string is too short.")

###7.2 Example: Return value with subfunctions
# -*- coding: cp1252 -*-

# def calculator(distance,gas,mpg):
#     price = gas*(distance/mpg)

#     price = int(price)
#     return price

# def main():
#     gasprice = float(input("How much is one gallon of gas?: "))
#     tripdistance = int(input("How many miles will be driven?: "))
#     averagempg = float(input("How many mpg does the car get?: "))

#     total_sum = calculator(tripdistance,gasprice,averagempg)
#     print("The trip will cost",total_sum,"euros.")

# if __name__ == "__main__":
#     main()


##8
# def printstuff(charline = "Defaults!"):
#     print(charline)
# printstuff("Testing my function!")
# printstuff()


##9 Example: Default values for parameters
# -*- coding: cp1252 -*-

def square(width= float(5.0), height = float(8.0)):
    area = width*height
    return area

def main():
    #Since we now have default values,
    #we can leave some of the parameters out.
    area1 = square()
    area2 = square(4.0,3.0)
    area3 = square(10.0)
    area4 = square(height = 11.0)

    print("Four different ways of calling our function...")
    print("And they all work:")
    print(area1,area2,area3,area4)

if __name__ == "__main__":
    main()