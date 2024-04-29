#15.2 Exercise: Using parameters
def poweroftwo(number):
    return 2**number
def main():
    currentnumber = int(input("Give a number: "))
    result = poweroftwo(currentnumber)
    print('The result is', result)
if __name__ == "__main__":
    main()