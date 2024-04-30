##8.2 Exercise: Nuke-foot-cockroach
# import random
# def computerchoice():
#     computerchoicenumber = random.randint(1,3)
#     if computerchoicenumber == 3:
#         computerchoice = 'Foot'
#     elif computerchoicenumber == 1:
#         computerchoice = 'Cockroach'
#     elif computerchoicenumber == 2:
#         computerchoice = 'Nuke'
#     print('Computer chose:', computerchoice)

# def yourchoice():
#     if yourchoice == 'Foot':
#         yourchoicenumber = 3
#     elif yourchoice == 'Cockroach':
#         yourchoicenumber = 1
#     elif yourchoice == 'Nuke':
#         yourchoicenumber = 2
#     print('You chose:', yourchoice)


# def main():
#     while True:
#         yourchoice = input('Foot, Nuke or Cockroach? (Quit ends):')
#         print('You chose:', yourchoice)
#         computerchoice()
#         if yourchoice == 'Foot':
#             yourchoicenumber = 3
#         elif yourchoice == 'Cockroach':
#             yourchoicenumber = 1
#         elif yourchoice == 'Nuke':
#             yourchoicenumber = 2
        
#         if yourchoicenumber == computerchoicenumber == 2:
#             print('Both LOSE!')
#         elif yourchoicenumber == computerchoicenumber:
#             print('It is a tie!')
#         elif yourchoicenumber > computerchoicenumber:
#             print('You WIN!')
#         elif yourchoicenumber < computerchoicenumber:
#             print('You LOSE!')

# if __name__ == "__main__":
#     main()



import random

def computerchoice():
    computer_choice_number = random.randint(1, 3)
    if computer_choice_number == 3:
        computer_choice = 'Foot'
    elif computer_choice_number == 1:
        computer_choice = 'Cockroach'
    elif computer_choice_number == 2:
        computer_choice = 'Nuke'
    print('Computer chose:', computer_choice)
    return computer_choice

def yourchoice():
    while True:
        choice = input('Foot, Nuke or Cockroach? (Quit ends): ')
        if choice.lower() == 'quit':  # Check for 'Quit' input
            return None
        elif choice in ['Foot', 'Nuke', 'Cockroach']:
            print('You chose:', choice)
            return choice
            
        else:
            print('Incorrect selection.')

def main():
    rounds = 0
    wins = 0
    ties = 0
    while True:
        user_choice = yourchoice()
        if user_choice is None:
            print(f'You played {rounds} rounds, and won {wins} rounds, playing tie in {ties} rounds.')
            break
        rounds +=1
        computer_choice_result = computerchoice()
        if user_choice == 'Nuke' and computer_choice_result == 'Nuke':
            print('Both LOSE!')
        elif user_choice == computer_choice_result:
            print('It is a tie!')
            ties +=1
        elif user_choice == 'Foot' and computer_choice_result == 'Cockroach' or user_choice == 'Nuke' and computer_choice_result == 'Foot' or user_choice == 'Cockroach' and computer_choice_result == 'Nuke' :
            print('You WIN!')
            wins +=1
        else:
            print('You LOSE!')
        

if __name__ == "__main__":
    main()
