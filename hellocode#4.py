# -*- coding: cp1252 -*-

##Requests the amount of repetitions
#totalrounds = int(input("How many rounds?: "))
#nowround = 0

##define the iteration argument;
##when the amount of done rounds becomes 
##higher than the given total, the iteration ends.

#while nowround < totalrounds:
    #print("Now is the round",nowround)
##The amount of done rounds adds 1
    #nowround += 1



##Example: Number multiplier with For
## -*- coding: cp1252 -*-

##Ask the amount of iterations from the user
#series = int(input("How many rounds are calculated?: "))

#result = int(1)
#for turn in range(1,series+1):
#    result = result*turn
#    print("At turn",turn,"the result is",str(result)+".")

#print("The final result is", result)



##Example: Infinite loop with ending criteria
# keepgoing = True

# while keepgoing:
#     userwrote = input("Write something: ")
#     if userwrote == "End":
#         keepgoing = False
#         print(userwrote)
#     else:
#         print(userwrote)

# rounds = 0
# keepgoing = True
# while keepgoing:
#     print("Iteration!")
#     if rounds == 6:
#         keepgoing = False
#     else:
#         rounds = rounds + 1

##8#Example: Break-command in action
# startpoint = int(input("Give the starting point: "))

# while True:
#     if startpoint % 13 == 0:
#         print("Currently we are at",startpoint)
#         print("We found a number divisible by 13!")
#         break
#     else:
#         print("Currently we are at",startpoint)
#         startpoint += 1

##9#
# total = 0
# i = 0
# rounds = int(input("How many rounds?: "))

# while i < rounds:
#     i += 1
#     #If the i is not round number, skip it
#     if i % 2 != 0:
#         continue
    
#     print("Added ",i,".", sep="")
#     total = total + i

# print("The sum was ",total,".", sep="")

##10#Example: Else in an iteration
## -*- coding: cp1252 -*-
# start = int(input("Enter starting position: "))
# end = int(input("Enter ending position: "))

# options = range(start,end)

# for i in options:
#     if i == 42:
#         print("We found 42!")
#         break
		
##Notice that this else is connected to for, not if
# else:
#     print("Seems that there was no answer in there.")



##12
##12.1
# totalrounds = 5
# nowround = 0
# while nowround < totalrounds:
#     print("This is lap ",nowround)
#     nowround += 1

##12.2
# keepgoing = True
# while keepgoing:
#     userwrote = input("Write something: ")
#     if userwrote == "quit":
#         keepgoing = False
#         print("Bye bye!")
#     else:
#         print(userwrote)

##12.3
# result = int(0)
# number = int(input("Give a number: "))
# for turn in range(0,number):
#     result = result+turn
# print("The sum was: ",result)

##12.4

print("Calculator")

number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
keepgoing = True
while keepgoing:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) Change numbers")
    print("(6) Quit")
    print("Current numbers: ", number1, number2)
    choice = int(input("Please select something (1-6): "))
    if choice == 6:
        print("Thank you!")
        break
    elif choice == 1:
        result1 = number1 + number2
        print("The result is: ", result1)
    elif choice == 2:
        result2 = number1 - number2
        print("The result is: ", result2)
    elif choice == 3:
        result3 = number1 * number2
        print("The result is: ", result3)
    elif choice == 4:
        result4 = number1 / number2
        print("The result is: ", result4)
    elif choice == 5:
        number1 = int(input("Give the first number: "))
        number2 = int(input("Give the second number: "))
        
    

  
