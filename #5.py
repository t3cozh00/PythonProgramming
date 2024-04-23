#1
sourcefile = open("example.txt","r")


#2
##Example: Opening and reading a file
# -*- coding: cp1252 -*-
# readfile = open("example.txt","r")
# content = readfile.readlines()

# print(content)
# for i in content:
#     print(i)

# readfile.close()


#3
# -*- coding: cp1252 -*-
# handle = open("example.txt","r")
# filetext = handle.read()
# print(filetext)
# handle.close()


#4
# readfile = open('example.txt','r')

# content = readfile.readline()
# location = readfile.tell()
# print(content[:-1]+"; The pointer is now at",location)

# print("Return to character number 10:")
# readfile.seek(10)
# content = readfile.read()
# print(content)

# readfile.close()


#5
##Example: Using the read numerical value
# -*- coding: cp1252 -*-
# number = 1024
# readfile = open("numberfile.txt","w")
# readfile.write( str(number) )
# readfile.close()

# readnumber = 0
# readfile = open("numberfile.txt","r")
# readnumber = int(readfile.readline())
# readfile.close()

# print("A number",readnumber," was read and converted to a number:")
# readnumber = readnumber *2
# print(readnumber)

# readfile = open("numberfile1.txt","w")
# number = 222
# readfile.write(str(number))


#6 Example: Creating and writing to a file
# -*- coding: cp1252 -*-
# myfile = open("writings.txt","w")
# mytext = "First line!\nSecond line!\nLast in line!"
# print(mytext)

# myfile.write(mytext)
# myfile.close()


#7 Example: Appending existing file
# -*- coding: cp1252 -*-
# myfile = open("writings.txt","a")
# addedtext = "Added line!\nThis goes to writings.txt! \
# which was created earlier.\n"
  
# print(addedtext)
  
# myfile.write(addedtext)
# myfile.close()

# handle = open("writings.txt","r")
# filetext1 = handle.read()
# print("filetext1: ",filetext1)
# handle.close()

# myfile = open("writings.txt", "a")
# myfile.write(filetext1)
# myfile.close()
# myfile = open("writings.txt", "r")
# filetext2 = myfile.read()
# print("filetext2: ", filetext2)
# myfile.close()


#11
#11.1 Exercise: Reading a file
# myfile = open("facts.txt", "r")
# filetext = myfile.read()
# print("Following was read from the file: ", filetext)
# myfile.close()

#11.2 Exercise: Writing to a file
# filename = input("Give a file name: ")
# filetext = input("Write something: ")
# handle = open(filename,"w")
# handle.write(filetext)
# print("Wrote ", filetext, " to the file", filename)
# handle.close()

#11.3 Exercise: Filtering the file contents
# readfile = open("example.txt","r")
# content = readfile.readlines()

# print(content)
# for i in content:
#     print(i)

# readfile.close()
# myfile = open("strings.txt", "r")
# linetext = myfile.readlines()
# myfile.close()

# for line in linetext:
#     if(line[:-1].isalnum()):
#         print(line, "was ok.")
#     else:
#         print(line, "was invalid.")

#11.4 Exercise: Notebook: Read and write to the notebook
keepgoing = True
while keepgoing:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit" + '\n')
    choice = int(input("Please select one: "))
    if choice == 4:
        print("Notebook shutting down, thank you.") 
        break
    elif choice == 1:
        myfile = open("notebook.txt", "r")
        choice1 = myfile.read()
        print(choice1)
        myfile.close()
    elif choice == 2:
        addtext = input("Write a new note: ")
        myfile = open("notebook.txt", "a")
        myfile.write(addtext + "\n")
        myfile.close()
    elif choice == 3:
        myfile = open("notebook.txt", "w")
        myfile.close()
        print("Notes deleted.")
        


