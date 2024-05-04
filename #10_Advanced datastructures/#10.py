##2  Example: Creating and using a list part one
#-*- coding: cp1252 -*-

# #List as a variable
# #Create mylist, notice the line break in the definition
# mylist = ["Apples","Milk",
#           "Beer","Squigg"]
# print(mylist)
  
# #Let's add one item
# mylist.append("Pineapple")
# print(mylist)

# #Let's remove item 1
# mylist.pop(1)

# #This prints the mylist
# for i in mylist:
#     print(i)


##3 
# basket = ["Apples", "Orange","Kiwifruit","Banana"]
# print("Cauliflower" in basket)
# print("Apples" in basket)

# mylist = [1,2,3,4]
# for i in mylist:
# 	print(i)

# newlist = []
# for i in mylist:
# 	newlist.append(i+10)
# print(newlist)


##4 
# diction = {"A":"Apples", "O":"Oranges"}
# print(diction["A"])

# Example: Morse characters and dictionary
#-*- coding: cp1252 -*-

# def morsecoder(word):
#     #函数 morsecoder 的参数 word 默认是一个字符串
# #Let's define some letters
#     alphabet = { 'a' : '.-', 'b' : '-...',
#                    'c' : '-.-.', 'd' : '-..',
#                    'e' : '.', 'f' : '..-.',
#                    'g' : '--.', 'h' : '....',
#                    'i' : '..', 'j' : '.---',
#                    'k' : '-.-', 'l' : '.-..'}

#     result = ""
#     for i in range(0,len(word)):
#         result = result + alphabet[word[i]]+"/"

#     print("Word",word,"in Morse code is")
#     print(result)

# worde_1 = "cliff"
# worde_2 = "bach"
# morsecoder(worde_1)
# morsecoder(worde_2)


##6 Example: Tuple in a program
# -*- coding: utf-8 -*-
# def tupleprint(data):
#     part1, part2, part3 = data
#     print(part1+":")
#     print(part2+" :: "+part3)

# name = "Old Jolly"
# address = "Mountaintop 1, FI-99999 Korvatunturi"
# phone = "555-1234567"

# datatuple = (name, address, phone)
# tupleprint(datatuple)

