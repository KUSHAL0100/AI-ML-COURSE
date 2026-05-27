class Myclass:
    def fun1(self,a):
        cnt=0
        for i in range(1,a):
            if a%i==0:
                cnt+=1
        
        if cnt==2:
            print("Prime number")
        else:
            print("Not a prime number")
    
    def fun2(self):
        for i in range(1,6):
            for k in range(1,6-i):
                print(" ",end="")
            for j in range(1,i+1):
                print("*",end=" ")
            print()
        # for i in range(4,0,-1): #For pyramid
        #     for k in range(1,6-i):
        #         print(" ",end="")
        #     for j in range(1,i+1):
        #         print("*",end=" ")
        #     print()
    
    def fun3(self,a):
        rev=0
        while a!=0:
            reminder=a%10
            rev=rev*10 + reminder
            a//=10 #a/=10 na lakhvu,nai to ee float ma convert krse
        print(rev)
        

obj=Myclass()
while True:
    print("""
1.Prime Number
2.Triangle
3.Reverse Number
4.Exit
""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        n=int(input("Enter your number: "))
        obj.fun1(n)
    elif choice==2:
        obj.fun2()
    elif choice==3:
        n=int(input("Enter your number: "))
        obj.fun3(n)
    elif choice==4:
        print("Thank you!!")
        break
    else:
        print("Invalid choice!!!")
        break
