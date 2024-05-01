##9.3 Exercise: Calculator: Checking input validity

from math import sin, cos 
print("Calculator")

def numbergetter():
    while True:
        try:
            numbervalue = int(input('Give a number: '))
            return numbervalue
        except Exception:
            print('This input is invalid.')
            

def calculate():
    number1 = numbergetter()
    number2 = numbergetter()
    while True:
        print("(1) +")
        print("(2) -")
        print("(3) *")
        print("(4) /")
        print("(5) sin(number1/number2)")
        print("(6) cos(number1/number2)")
        print("(7) Change numbers")
        print("(8) Quit")
        print("Current numbers: ", number1, number2)
        choice = int(input("Please select something (1-6): "))
        if choice == 8:
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
            
            result5 = sin(number1 / number2)
            print("The result is: ", result5)
        elif choice == 6:
            
            result6 = cos(number1 / number2)
            print("The result is: ", result6)
        elif choice == 7:
            number1 = numbergetter()
            number2 = numbergetter()
if __name__ == "__main__":
    calculate()       