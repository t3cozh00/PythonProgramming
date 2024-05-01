##9.4 Exercise: Notebook: Changing the written file.
import time
print ('No default notebook was found, create one.')
filename = 'notebook.txt'

def choosefile():
    global filename
    print('Now using file', filename)

def openfile():
        global filename
        try:
            newfilename = input('Give the name of the new file: ')
            myfile = open(newfilename, 'r')
            myfile.close()
            filename = newfilename
        except IOError:
            print('No notebook with that name detected, created one.')
            filename = newfilename
            myfile = open(filename, 'w')
            myfile.close()

def main():
    while True:
        choosefile()
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Empty the notebook")
        print("(4) Change the notebook")
        print("(5) Quit\n")

        choice = int(input('Please select one: '))
        if choice == 5:
            print('Notebook shutting down, thank you.')
            break
        elif choice == 1:
            myfile = open(filename, 'r')
            choice1 = myfile.read()
            print(choice1)
            myfile.close()
        elif choice == 2:
            addtext = input("Write a new note: ")
            myfile = open(filename, "a")
            myfile.write(addtext + ':::' + time.strftime("%X %x") + '\n')
            myfile.close()
        elif choice == 4:
            openfile()

if __name__ == "__main__":
    main()   