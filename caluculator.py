def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division (a,b):
    if b==0:
        return "Error Error"
    else:
        return a/b
num1=int(input("enter the value  of a :"))
num2=int(input("enter the value  of b :"))
operation=input("enter the operation (+,-,*,/): ")
if operation=="+":
    print(add(num1,num2))
elif operation=="-":
    print(subract(num1,num2))
elif operation=="*":
    print(multiplication(num1,num2))
else:
    print(division(num1,num2))