##9.1 Exercise: Basic exception handler
mynumber = input('Give a number: ')
try:
    int(mynumber)
    print('The input was suitable!')
except Exception:
    print('The input was malformed.')