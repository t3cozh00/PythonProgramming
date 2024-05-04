##10.2 Exercise: Using the list
mylist = []
while True:
    print('Would you like to')
    print('(1)Add or')
    print('(2)Remove items or')
    mychoice = int(input('(3)Quit?: '))

    if mychoice == 3:
        print('The following items remain in the list: ')
        for i in mylist:
            print(i)
        break
    elif mychoice == 1:
        additem = input('What will be added?: ')
        mylist.append(additem)
    elif mychoice == 2:
        print('There are', len(mylist), 'items in the list.')
        deleteitemindex = int(input('Which item is deleted?: '))
        if deleteitemindex >= len(mylist):
            print('Incorrect selection.')
        else:
            mylist.remove(mylist[deleteitemindex])
        
    else:
        print('Incorrect selection.')


    