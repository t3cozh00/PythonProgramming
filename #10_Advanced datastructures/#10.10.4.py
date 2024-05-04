##10.4 Exercise: Notebook: Using list with the notebook, pickle
import pickle, time
import os.path

def checkfile():
    if not os.path.exists('notebook.dat'):
        print('No default notebook was found, created one.')
        datfilename = open('notebook.dat', 'wb')
        pickle.dump([], datfilename)
        datfilename.close()

def main():
    while True:
        checkfile()
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Edit a note")
        print("(4) Delete a note")
        print("(5) Save and quit\n")
        choice = int(input('Please select one: '))

        if choice == 5:
            print('Notebook shutting down, thank you.')
            break

        else:
            picklefile = open('notebook.dat', 'rb')
            todolist = pickle.load(picklefile)

            if choice == 1:
                for i in todolist:
                    print(i)
            elif choice == 2:
                addtext = input("Write a new note: ")
                todolist.append(addtext + ':::' + time.strftime("%X %x"))
            else:
                print('The list has', len(todolist), 'notes.')
                if choice == 3:
                    editnoteindex = int(input('Which of them will be changed?: '))
                    print(todolist[editnoteindex])
                    addtext = input("Give the new note: ")
                    todolist[editnoteindex] = addtext + ':::' + time.strftime("%X %x")
                elif choice == 4:
                    deletenoteindex = int(input('Which of them will be deleted?: '))
                    if deletenoteindex == len(todolist):
                        print('Deleted note', todolist[deletenoteindex-1])
                        todolist.remove(todolist[deletenoteindex-1])
                    else:
                        print('Deleted note', todolist[deletenoteindex])
                        todolist.remove(todolist[deletenoteindex])

            filename = open('notebook.dat', 'wb')
            pickle.dump(todolist, filename)
            filename.close()

if __name__ == '__main__':
    main()

        
            



        
