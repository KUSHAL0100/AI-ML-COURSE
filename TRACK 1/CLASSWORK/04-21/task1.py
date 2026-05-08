menu="""
Enter 1 for Factorial
Enter 2 for Prime Number
Enter 3 for Reverse Number
Enter 4 to Exit

"""

while True:
    print(menu)
    choice=int(input("Enter the choice: "))
    if choice==1:
        n=int(input("Enter the number: "))
        fact=1
        for i in range(1,n+1):
            fact*=i
        print(fact)

    elif choice==2:
        n=int(input("Enter the number: "))
        cnt=0
        for i in range(1,n+1):
            if n%2==0: cnt+=1
        if cnt==2: print("Prime Number")
        else: print("Not a Prime Number")

    elif choice==3:
        n=int(input("Enter the number: "))
        rev=0
        while n!=0:
            rev= (rev*10) + (n%10)
            n//=10 
        print(rev)
    elif choice==4:
        print("Thank youuuu!!")
        break
    else:
        print("Invalid choice")
        break
