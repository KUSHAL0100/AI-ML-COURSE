from pathlib import Path
import random
import json
import string

# __file__ means current python file's path,then by writting it inside path()[e.g. "8thapril/bnkingmgt.py"],it converts it into the path,then .parent means,get the parent folder[e.g from "8thapril/bankingmgt.py" =>> to "bankingmgt/"], and then /data.json ['means create file with this name or open']
path=Path(__file__).parent / "data.json"

# data = []

if path.exists() and path.read_text():
    # with open(path, "r") as fs:
    #     data = json.load(fs)  #Both are same,this one and below one
    data=json.loads(path.read_text())   
else: data=[]
# print(data) Both will return lists of dictionaries
class Bank:
    
    @classmethod
    def __readAccount(cls,accno,pin):
        
        # print(data)
        # result=list(filter(lambda acc:acc["name"]==name and acc["pin"]==pin,data)) #filter returns an obj,which is not in format of readable,so need to convert it into list first
        # return result[0] if result else None 


        # more better approach,use NEXT,iterator me se next first value fetch krke check krta hai,in our case all of them are obj,so next returns obj and list returns list
        result=next(filter(lambda acc:acc["accno"]==accno and acc["pin"]==pin,data),None) #the none we wrote is for next,if nothing found in iteration,return None
        return result if result else None
    
    def creatingAccount(self,name,email,pin):
        self.name=name
        self.email=email
        self.__pin=pin
        allchars=string.ascii_letters+string.digits+"!*%@,"
        self.__accno= ''.join(random.choice(allchars) for _ in range(10))
        self.__balance=0
        new_Acc={
            "name":self.name,
            "email":self.email,
            "pin":self.__pin,
            "accno":self.__accno,
            "balance":self.__balance
        }
        data.append(new_Acc)
        path.write_text(json.dumps(data,indent=4))
        print(f"Your Account is Created ,Please Note Down Your AccNo. : {Bank.__readAccount(self.__accno,self.__pin)}")

    def depositMoney(self,accno,pin,amount):
        # for i in data:
        #     if[data["accno"]==accno and data["pin"]==pin]:
        #         data["balance"]+=amount #this will fail because,our json file is , list of dictinary,so every user is dictionary but it is inside list

        # for i in data:
        #     if(i["accno"]==accno): 
        #         i["balance"]+=amount
        #         print(f"Your amount deposited succesfully,Your balance is: {i["balance"]}")
        #     else: print("No account found with this accno and pin")

        #Found Out after Update Account Function
        dummydata=Bank.__readAccount(accno,pin)
        if not dummydata:
            print("Account not found ")
            return
        dummydata["balance"]+=amount
        print(f"Your Amount Deposited Sucessfully, with new Balance: {dummydata['balance']}")

        path.write_text(json.dumps(data,indent=4))
        
    def withdrawMoney(self,accno,pin,amount):
        # for i in data:
        #     if(i["accno"]==accno and i["pin"]==pin): 
        #         if i["balance"] >=amount:
        #             i["balance"]-=amount
        #             print(f"Your amount Deposited succesfully,Your balance is: {i["balance"]}")
        #         else: print("Insufficient Balance!!!")
        #     else: print("No account found with this accno and pin")

        #Found Out after Update Account Function
        dummydata=Bank.__readAccount(accno,pin)
        if not dummydata:
            print("Account not found ")
            return
        if(dummydata["balance"]>=amount):
            dummydata["balance"]-=amount
            print(f"Your Amount Withdrawn Sucessfully, with new Balance: {dummydata['balance']}")
        else: print("Insufficient Balance")
        path.write_text(json.dumps(data,indent=4))
    
    def fetchUser(self,accno,pin):
        if Bank.__readAccount(accno,pin):
            print(f"Your Account Information is: : {Bank.__readAccount(accno,pin)}")
        else: print("No account found with this accno and pin")
    
    def updateUser(self,accno,pin,name,email,new_pin):
        # dummydata = next(
        # filter(lambda acc: acc["accno"] == accno and acc["pin"] == str(pin), data),
        # None
        # )
    #Above Code also creates DeepCopy,and makes dummydata a new ref for that specific data,till now i thought only dummydata=data will create ref,but no above code also creates ref LOL
    #So now we can directly use __readacc func too as it can also creater ref

        dummydata=Bank.__readAccount(accno,pin) #it is dummydata=data[index] indirectly, just wow
        if not dummydata:
            print("Account not found ")
            return

        # update name
        if name.strip() != "":
            dummydata["name"] = name

        # update email
        if email.strip() != "":
            dummydata["email"] = email
        if len(new_pin.strip())!=4: 
            print("Pin must be 4 digits") 
            return

        if new_pin.strip()!="":
            try:
                dummydata["pin"]=int(new_pin)
            except ValueError:
                print("Pin must be in digits!!")
                return
        path.write_text(json.dumps(data,indent=4))

    def deleteUser(self,accno,pin):
        dummydata=Bank.__readAccount(accno,pin)
        if not dummydata:
            print("Account not found")
            return
        print("Are you sure want to delete account? press Y/N")
        res=input("Tell us your answer in Y or N: ").lower()
        if res=="y":
            # dummydata=None #This will not work lol,it removes ref,not data
            data.remove(dummydata)
            print("Account Deelted Sucessfully!!")
            path.write_text(json.dumps(data,indent=4))
        else: print("Deletion Cancelled!!")
        

user=Bank()
while True:
    print("\nPress 0 to exit")
    print("Press 1 for creating account")
    print("Press 2 for Depositing money")
    print("Press 3 for withdrawing money")
    print("Press 4 for checking details")
    print("Press 5 for updating details")
    print("Press 6 for deleting account")
    try:
        res=int(input("Enter your choice: "))
    except ValueError: 
        print("Enter Choice in digits only")
        continue
    #We can also use match case by, Match res: case 1:,case 2:,case _: etc etc
    if res==0:
        print("Exiting....")
        break
    elif res==1:
        name=input("Enter Your Name: ")
        email=input("Enter Your email: ")
        pin=int(input("Enter Your Pin: "))
        user.creatingAccount(name,email,pin)

    elif res==2:
        accno=input("Enter Your Acc No: ")
        pin=int(input("Enter Your Account Pin: "))
        amount=int(input("Enter Your Ammount to Deposit: "))
        if amount<10000 and amount>0:
            user.depositMoney(accno,pin,amount)
        else: print("Enter Amount below 10,000 and above 0")

    elif res==3:
        accno=input("Enter Your Acc No: ")
        pin=int(input("Enter Your Account Pin: "))
        amount=int(input("Enter Your Ammount to Withdraw: "))
        if amount<10000 and amount>0:
            user.withdrawMoney(accno,pin,amount)
        else: print("Enter Amount below 10,000 and above 0")

    elif res==4:
        accno=input("Enter Your Acc No: ")
        pin=int(input("Enter Your Account Pin: "))
        user.fetchUser(accno,pin)

    elif res==5:
        print("Press the Enter if you dont'want to change that Detail,otherwise write it down")
        accno=input("Enter Your Acc No. to find your acc: ")
        pin=int(input("Enter Your Account Current Pin: "))
        name=input("Enter The Name to change: ")
        email=input("Enter The email to change: ")
        new_pin=input("Enter the pin to change: ")
        user.updateUser(accno,pin,name,email,new_pin)

    elif res==6:
        accno=input("Enter Your Acc No.: ")
        pin=int(input("Enter Your Account Current Pin: "))
        user.deleteUser(accno,pin)
    print("\n------------------------------------------------>")