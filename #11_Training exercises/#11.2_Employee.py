###1
# class Employee:
#     id = 0
#     name = ''

# userlist = []
# while True:
#     username = input('Please enter employee name (0 to quit):') 
#     if username == '0':
#         for i in range(0, len(userlist)):
#             print('Id: ', i+1, 'Name: ', userlist[i]) 
#     else:
#         userlist.append(username)

###2
class Employee:
    id = 0
    name = ''
    
    userlist = []
    def addusers(self):
        username = input('Please enter employee name (0 to quit):')
        if username == '0':
            return False
        self.userlist.append(username)
        return True
    
    def printout(self):
        for i in range(0, len(self.userlist)):
            print('Id: ', i+1, 'Name: ', self.userlist[i])

def main():
    users = Employee()
    while users.addusers():
        pass
    users.printout()

if __name__ == '__main__':
    main()


###3
class Employee:
    def __init__(self, id, name):
# Put your code here
        self.id = id
        self.name = name

employee_list = []
while True:
    username = input('Please enter employee name (0 to quit): ')
    if username == '0':
        break
    employee = Employee(len(employee_list) + 1, username)
    employee_list.append(employee)

for employee in employee_list:
    print("Id:",employee.id, "Name:", employee.name)
    

