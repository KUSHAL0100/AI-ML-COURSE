from pickle import OBJ
import random
acc_number=random.randint(1001,9999)
class Bank:
    def ac_register(self):
        self.name=input("Enter the name: ")
        self.email=input("Enter the email: ")
        self.password=input("enter password: ")
        self.acno=acc_number
        self.balance=5000

        print(f"Your acc number: {self.acno}")
        print(f"Password is: {self.password}")
    
    def deposit(self):
        ac_no=int(input("Enter the Ac No: "))
        password=input("Enter the Password: ")

        if ac_no==self.acno and password==self.password:
            deposit=int(input("Enter the deposit Ammount: "))

            if deposit>=10000:
                print("Amount should be less then 10,000")
            else:
                self.balance+=deposit
                print(f"Balance: {self.balance}")
        else:
            print("Wrong acc info")
    
    def withdraw(self):
        ac_no=int(input("Enter the Ac No: "))
        password=input("Enter the Password: ")

        if ac_no==self.acno and password==self.password:
            withdraw=int(input("Enter the withdraw Ammount: "))

            if withdraw>=10000:
                print("Amount should be less then 10,000")
            else:
                self.balance-=withdraw
                print(f"Balance: {self.balance}")
        else:
            print("Wrong acc info")

obj=Bank()
print(""""
1. for opening account
2. for exit      
      """)
choice=int(input("Enter your choice: "))

if choice==1:
    obj.ac_register()
    while True:
        print("""
1.Deposit Money
2.Withdraw Money
3.Exit
    """)
        n=int(input("Enter your choice: "))
        if n==1:
            obj.deposit()
        elif n==2:
            obj.withdraw()
        else:
            print("Thank you!!")
            break

else:
    print("Thank you!!!")
    