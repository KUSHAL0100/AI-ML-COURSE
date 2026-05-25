import random

otp=random.randint(1001,9999)

d={}
while True:
    print(""""
1.Create Account
2.Login
3.Forgot Password
4.Exit
""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter your name: ")
        email=input("Enter your email: ")
        phoneno=int(input("Enter your phone no.: "))
        password=input("Enter your password: ")
        cpassword=input("Confirm your Password: ")

        if password==cpassword:
            d['email']=email
            d['phoneno']=phoneno
            d['password']=password
            print("Account Created!!")
        else:
            print("Enter both password correctly!")
    elif choice==2:
        email=input("Enter your email: ")
        password=input("Enter your password: ")

        if d['email']==email and d['password']==password:
            print("Login succesfull!!")
        else: 
            print("Invalid Credentials!!")
    elif choice==3:
        phoneno=int(input("Enter your phone no.: "))
        if d['phoneno'] == phoneno:
            print(f"Your otp is: {otp}")
            ans=int(input("Enter the otp: "))
            if ans==otp:
                password=input("Enter the new password: ")
                d["password"]=password
                print("Password successfully changed!!")
            else:
                print("Wrong otp!!")
        else:
            print("Wrong phone no!!")
    elif choice==4:
        print("Thank you!!")
        break
    else:
        print("Invalid choice!!")
        break
