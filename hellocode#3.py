# -*- coding: cp1252 -*-

# color = input("What is your favorite color?: ")
#Let's define the selection argument and see if it was "blue"
#Notice the new indentation level inside the structure
# if color == "Blue":
#     print("Blue is nice.")

# print("This line follows the if-structure and is always executed.")


#3-4
# -*- coding: cp1252 -*-

# color = input("What is your favorite color?: ")

# #Make note of the indentation in the structure
# if color == "Blue":
#     print("Blue is also my personal favorite.")
# else:
#     print(color,"is also nice.")

# print("This print is after the if-structure and is always printed.") 


#3-5
# -*- coding: cp1252 -*-

# color = input("What is your favorite color?: ")

# if color == "Blue":
#     print("Blue is also my personal favorite.")

# elif color == "Red":
#     print("Red looks good on a sports car.")
# elif color == "Salmon":
#     print("Most would say that salmon is a fish, but I guess it also counts as a color.")

# else:
#     print(color,"is also nice.")


# #3-7
# value = 1
# if value == 1: result = True
# print(result)


#
# value = input("Give a number:")
# if value % 2 == 0:
#    print("The given number was even.")


#3-11
# print("Calculator")
# number1 = int(input("Give the first number: "))
# number2 = int(input("Give the second number: "))
# print("(1) +")
# print("(2) -")
# print("(3) *")
# print("(4) /")
# operator = int(input("Please select something (1-4): "))
# if operator == 1:
#     result1 = number1 + number2
#     print("The result is: ", result1)
# elif operator == 2:
#     result2 = number1 - number2
#     print("The result is: ", result2)
# elif operator == 3:
#     result3 = number1 * number2
#     print("The result is: ", result3)
# elif operator == 4:
#     result4 = number1 / number2
#     print("The result is: ", result4)
# else:
#     print("Selection was not correct.")

#3-12
color = "black"
if color == "black":
    print("A bit gloomy here.")

name = "Carl"
if name == "Matt":
    print("Hi Matt!")
else:
    print("Oh you are somebody else.")

selection = "tricycle"

if selection == "money":
    print("You selected the money!")
elif selection == "tricycle":
    print("You selected the tricycle!")
else:
    print("Nothing.")

textline = "applejuice"

if textline == applejuice:
    print("My favorite!")

textline = "applejuice"

if textline = "applejuice":
    print("My favorite!")