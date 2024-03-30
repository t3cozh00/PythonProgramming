# print("This is our first Python program,")
# print("Hello World!")

# # -*- coding: cp1252 -*-
# print("This is our first Python program,")
# print("Hello World!")

# #2 Fundamentals of the Python language
# # -*- coding: cp1252 -*-
# print("This line will be printed.")
# #This is a comment, interpreter cannot see me!

# print("This is the second printed line.")
# #print("This print command is commented away.")

# #The next line has an inline comment:
# print("This is the third printed line.") #Comment!

# # This comment is divided
# # into several lines of code. The interpreter does not
# # care about this as long as every line starts with "#".
# print("This is the last printed line.")

# 2-9 Presenting strings 
# if True:
#    print("This is a very big and long, even annoying\
# command which takes way too much space \
# and is irritating to handle. And now its full \
# of holes.")

# print("This is a very big, long and even annoying \
# command which takes way too much space and is irritating to handle.")

# 2-10 Predefined string
# print("""There are several things that should be checked when
# buying a car:
# -maintenance record
# -rust spots
# -possible needs for maintenance
# Also one should:
# -ensure that the car sale is legit
# -insurance is ok
# -the car "feels" normal on a test drive""")

# 2-11 Escaping layout characters
# print("So are we supposed to see \
# '\\' this or what? What does this \do?")

# 2-12 Hangling inputs
# givenvalue = input("Write something: ")
# givenvalue = input("")
# print (givenvalue)

# Example: Taking string as an input
# -*- coding: cp1252 -*-
# creates a variable, and saves the user-written
# text as a value to the variable
# nimi = input("What is your name? --")
# print("Hello",nimi+"!")
# print("Nice to see you.")

# 2-13 Type conversions, str(), int() and float()
# value = input("Give a number: ")
# value = int(value)
# print(value + 10)

# 2-14
# number = "300"
# int(number)
# print (number)

# number = 4.9995
# print(int(number))

# 2-15
# bigstring = "auxilia"
# print(len(bigstring))

# 2-16
# bigstring = "auxiliaryemergencyfirepreventionsystem"
# print(bigstring[38:0:-1])
# print(bigstring[::-1])

# 2-17
# Example: Collection of different string slices
# -*- coding: cp1252 -*-
# bigstring = "Damn the torpedoes, full speed ahead!"
# length = len(bigstring)
# print("The length of the string is",length,"characters.")

# slice_1 = bigstring[:15]
# slice_2 = bigstring[15:]
# slice_3 = bigstring[::2]

# slice_4 = bigstring[1]
# slice_5 = bigstring[5:26]
# slice_6 = bigstring[::-1]

# slice_7 = bigstring[-10:]
# slice_8 = bigstring[:-10]
# slice_9 = bigstring[4:30:2]

# print("slice_1: ",slice_1)
# print("slice_2: ",slice_2)
# print("slice_3: ",slice_3)
# print("slice_4: ",slice_4)
# print("slice_5: ",slice_5)
# print("slice_6: ",slice_6)
# print("slice_7: ",slice_7)
# print("slice_8: ",slice_8)
# print("slice_9: ",slice_9)

#2-18
# text = "testing"
# result = text.isalpha()
# print(result)

value = input("Write something and press enter: ")
print(value)