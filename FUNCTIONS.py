SAVE THIS IN FUNCTIONS.PY

def add(a,b):
    c=a+b
    print("sum=",c)

def sub(a,b):
    c=a-b
    print("diffrnce=",c)

def mul(a,b):
    c=a*b
    print("product=",c)

def div(a,b):
    c=a/b
    print("ans:",c)

    





THIS IS 2ND FILE
import functions as p

while True:
    a=int(input("enter fno"))
    b=int(input("enter sno"))
    print("enter ur option")

    ch=int(input("1.sum 2.subtract 3.mul 4.div"))
    match ch:
        case 1: p.add(a,b)
        case 2: p.sub(a,b)
        case 3: p.mul(a,b)
        case 4: p.div(a,b)
     
     
