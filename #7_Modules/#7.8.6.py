##8.6 Exercise: Notebook: Adding dates to the system
import time
while True:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit\n")

    choice = int(input('Please select one: '))
    if choice == 4:
        print('Notebook shutting down, thank you.')
        break
    elif choice == 1:
        myfile = open('notebook.txt', 'r')
        choice1 = myfile.read()
        print(choice1)
        myfile.close()
    elif choice == 2:
        addtext = input("Write a new note: ")
        myfile = open("notebook.txt", "a")
        myfile.write(addtext + ':::' + time.strftime("%X %x"))
        myfile.close()
