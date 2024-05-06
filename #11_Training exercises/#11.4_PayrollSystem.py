class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PayrollSystem:
    def calculate_payroll(employees):
        for employee in employees:
            print('Employee Payroll\n================')
            print('Payroll for:',employee.id, '-', employee.name)
            print('- Check amount:', employee.monthly_salary,'\n')
            

class SalaryEmployee(Employee):
    monthly_salary = 0
    def calculate_salary(self):
        self.monthly_salary = input('Please enter salary:')        

def main():
    employee_list = []
    while True:
        username = input('Please enter employee name (0 to quit):') 
        if username == '0':
            break
        employee = SalaryEmployee(len(employee_list) + 1, username)
        employee.calculate_salary()
        employee_list.append(employee)

    PayrollSystem.calculate_payroll(employee_list)

if __name__ == "__main__":
    main()

