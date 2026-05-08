def fibonacci(n):
    a=0
    b=1
    print(f"1: {a}")
    print(f"2: {b}")
    for i in range(3,n+1):
        sum=a+b
        a=b
        b=sum
        print(f"{i}: {b}")

def summ(n):
    sum=0
    for i in range(n):
        sum+=i
    print(f"Sum is: {sum}")

def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

menu="""
Enter 1 for Fibonaaci
Enter 2 for Sum till N Number
Enter 3 For Table
Enter 4 for Exit
"""

while True:
    print(menu)
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        n=int(input("Enter How many number: "))
        fibonacci(n)
    elif choice==2:
        n=int(input("Enter How many number: "))
        summ(n)
    elif choice==3:
        n=int(input("Enter Table Number: "))
        table(n)
    elif choice==4:
        print("Thank you!!")
        break
    else:
        print("Invalid choice!!")
        break

