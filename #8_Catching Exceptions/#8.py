##2  Example: Catching an error
# -*- coding: cp1252 -*-

# #Let's ask a value for mynumber
# mynumber = input("Give a numeric value: ")

# #convert the value to integer
# try:
#     mynumber = int(mynumber)
#     print("You gave a number",mynumber)

# #In case any error happens, the Exception
# #-named exception segment is run
# except Exception:
#     print("That was not a number!")

##3 Example: Handling several types of errors at once
# -*- coding: cp1252 -*-

# def getnumber():
#     mynumber = input("Give a numeric value: ")
#     return mynumber

# def main():
#     number1 = getnumber()
#     number2 = getnumber()
#     try:
#         result = int(number1) / int(number2)

#     except ZeroDivisionError:
#         print("Its not possible to divide with 0.")
  
#     except (TypeError, ValueError):
#         print("Its not possible to calculate letters.")

#     else:
#         print("The result is",result)

# if __name__ == "__main__":
#     main()


##5 Example: Else-segment in an exception handler
# -*- coding: cp1252 -*-
  
# number = input("Give a number value: ")

# try:
#     number = int(number)
# except Exception:
#     print("That was not a number.")
# #else happens if no except is used
# else:
#     print("You gave a number",number)


##6 Example: Ending on an error
# -*- coding: cp1252 -*-

#lets ask for an input
# number = input("Give a value: ")

# #let's try to convert the input to an integer
# try:
#     number = int(number)
#     print("You gave a value",number)
  
# #if anything happens, finally is executed
# finally:
#     print("There was an error in the program!")


##7 Example: Asking a numeric value
# -*- coding: cp1252 -*-
def numbergetter():
    while True:
        try:
            numbervalue = input('Give a numeric value: ')
            numbervalue = float(numbervalue)
            return numbervalue
        except Exception:
            print('Erroneous input, try again')
def main():
    print('Please type in the full salary')
    salary = numbergetter()
    print('Input the amount of taxes(0-100)')
    taxes = numbergetter()
    leftover = salary * ((100 - taxes) / 100)
    print('You are left with', leftover, 'euroes.')

if __name__ == '__main__':
    main()