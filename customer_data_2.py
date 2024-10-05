def read_customer_data():
    customers=[]
    n=int(input("enter no of customers= "))
    for i in range(n):
        name=input("enter the name of customer: ")
        age=int(input("enter the age of customer: "))

        customer = [name,age]
        customers.append(customer)
    return customers

def display_customers():
    customers=read_customer_data()

    print(customers)

display_customers()    
