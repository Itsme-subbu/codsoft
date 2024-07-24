def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        print("zero division error")
    else:    
        return a/b  
print("calculator operations")              
print("1.Addition")
print("2.substraction")
print("3.Multiplication")
print("4.Division")
while True:
    choice=int(input("enter the number(1-2-3-4) : "))
    if choice >=5:
        print("invalid choice ! please enter a number btw 1 - 4")
    else:
        num1=int(input("enter first number : "))
        num2=int(input("enter second number : "))    
        if choice == 1:
            print("you choose addition operation")
            total= add(num1,num2)
            print(f"{num1} + {num2} = {total}")
        elif choice == 2:
            print("you choose substraction operation")
            total= sub(num1,num2)
            print(f"{num1} - {num2} = {total}")
        elif choice == 3:
            print("you choose multiplication operation")
            total= multiply(num1,num2)
            print(f"{num1} * {num2} = {total}")       
        else:
            print("you choose division operation")
            total=divide(num1,num2)
            print(f"{num1} / {num2} = {total}")    