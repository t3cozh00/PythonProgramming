#15.4 Exercise: Return value
def tester(givenstring="Too short"):
    if len(givenstring) > 10:
        if 'X' in givenstring:
            print(givenstring)
            print("X spotted!")
            return True
        else:
            print(givenstring)
            return False
    elif len(givenstring) < 10:
        print("Too short")
        return False
    else:
        print(givenstring)

def main():
    while True:
        userinput = input('Write something (quit ends): ')
        if userinput == 'quit':
            break
        tester(userinput)



# def tester(givenstring="Too short"):
#     if len(givenstring) >= 10:
#         if 'X' in givenstring:
#             print(givenstring)
#             print("X spotted!")
#             return True
#         else:
#             print(givenstring)
#             return True
#     else:
#         print(givenstring)
#         return False

# def main():
#     while True:
#         userinput = input('Write something (quit ends): ')
#         if userinput == 'quit':
#             break
#         elif tester(userinput) == False:
#             tester()

# if __name__ == "__main__":
#     main()
