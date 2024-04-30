#15.3 Exercise: Default parameters
def tester(givenstring = "Too short"):
        print(givenstring)
    
def main():
    while True:
        userinput = input('Write something (quit ends): ')
        if userinput == 'quit':
            break
        elif len(userinput) < 10:
            tester()
        elif len(userinput) >= 10:
            tester(userinput)
if __name__ == "__main__":
    main()