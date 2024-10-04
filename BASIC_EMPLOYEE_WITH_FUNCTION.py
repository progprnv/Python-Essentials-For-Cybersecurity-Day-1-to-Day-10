SAVE THIS IN ONE FILE NAMED # EMPLOYEE.PY

def read_employee():
    company = []
    n = int(input("Enter number of employees: "))
    for i in range(n):
        name = input("Enter name: ")
        emp_no = input("Enter employee code: ")
        desig = input("Enter designation: ")
        bpay = float(input("Enter basic pay: "))  # Changed to float for financial values
        hra = float(input("Enter HRA: "))
        ta = float(input("Enter TA: "))
        da = float(input("Enter deduction amount: "))
        
        employee = {
            "name": name,
            "empno": emp_no,
            "desig": desig,
            "bpay": bpay,
            "hra": hra,
            "ta": ta,
            "ded": da
        }
        
        company.append(employee)
    return company

def display():
    employees = read_employee()
    for emp in employees:def read_employee():
    company = []
    n = int(input("Enter number of employees: "))
    for i in range(n):
        name = input("Enter name: ")
        emp_no = input("Enter employee code: ")
        desig = input("Enter designation: ")
        bpay = float(input("Enter basic pay: "))  # Changed to float for financial values
        hra = float(input("Enter HRA: "))
        ta = float(input("Enter TA: "))
        da = float(input("Enter deduction amount: "))
        
        employee = {
            "name": name,
            "empno": emp_no,
            "desig": desig,
            "bpay": bpay,
            "hra": hra,
            "ta": ta,
            "ded": da
        }
        
        company.append(employee)
    return company

def display():
    employees = read_employee()
    for emp in employees:
        print("Name:", emp["name"])
        print("Emp No:", emp["empno"])
        print("Designation:", emp["desig"])
        print("Basic Pay:", emp["bpay"])
        print("HRA:", emp["hra"])
        print("TA:", emp["ta"])
        print("Deductions:", emp["ded"])
        
        net_pay = (emp["bpay"] + emp["hra"] + emp["ta"]) - emp["ded"]
        print("Net Pay:", net_pay)

# Call the display function to start the program
# display()

        print("Name:", emp["name"])
        print("Emp No:", emp["empno"])
        print("Designation:", emp["desig"])
        print("Basic Pay:", emp["bpay"])
        print("HRA:", emp["hra"])
        print("TA:", emp["ta"])
        print("Deductions:", emp["ded"])
        
        net_pay = (emp["bpay"] + emp["hra"] + emp["ta"]) - emp["ded"]
        print("Net Pay:", net_pay)

# Call the display function to start the program
# display()
-------------------------------------------------------------

save this file NAMED AS: EMPSEARCH.PY

import employee as e

def search():
    d=e.read_employee()
    n=(input("Enter name of employee to search: "))
    for emp in d:
        if emp['name']==n:
            print("Name:", emp["name"])
            print("Emp No:", emp["empno"])
            print("Designation:", emp["desig"])
            print("Basic Pay:", emp["bpay"])
            print("HRA:", emp["hra"])
            print("TA:", emp["ta"])
            print("Deductions:", emp["ded"])
            
            net_pay = (emp["bpay"] + emp["hra"] + emp["ta"]) - emp["ded"]
            print("Net Pay:", net_pay)
search()

