#Question 1:

# n=int(input("How many numbers you want to enter: "))
# sum=0
# for i in range(n):
#     inp=int(input(f"Enter the {i+1}th number: "))
#     sum+=inp

# print(f"Sum of {n} number is: {sum}")



#Question 2:

# str=input("Enter the string: ")
# sub=input("Enter the substring: ")
# print(f"The substring occured: {str.count(sub)}")


#Question 3:

# str=input("Enter the string: ")
# occr={}
# for i in range(len(str)):
#     ch=str[i]
#     if ch in occr:
#         occr[ch]+=1
#     else:
#         occr[ch]=1
# print(occr)


#Question 4:

# str=input("Enter the string: ")
# firstString=""
# secondString=""

# for i in range(len(str)):
#     if str[i]==" ":
#         firstString=str[0:i+1]
#         secondString=str[i+1:] #-1 nai lakhvu,nai to last letter nai ave
# # firstString[0],firstString[1]=firstString[1],firstString[0]
# # secondString[0],secondString[1]=secondString[1],secondString[0]
# #String is immutable,can't change it directly like text[0]="h"


# firstString= firstString[1]+firstString[0]+firstString[2:]
# secondString=secondString[1]+secondString[0]+secondString[2:]

# print(firstString)
# print(secondString)

#Question 5:

# str=input("Enter the string: ")

# if len(str)<=3:
#     print(str)
# else:
#     if str[-3:] == "ing":
#         str=str[0:-3] + "ly"
#     else:
#         str=str + "ing"
#     print(str)

#Question 6:

# str="Hello i am not poor"
# a=str.find("not")
# b=str.find("poor")

# if a<b:
#     c=str.find("not poor")
#     str= str[0:c] + "good"
# print(a)
# print(b)
# print(str)


#Question 7:

# a=int(input("Enter the First Number: "))
# b=int(input("Enter the Second Number: "))

# gcd=0
# for i in range(1,a+1):
#     if a%i==0 and b%i==0:
#         gcd=i

# print(gcd)


#Question 8:

# lst=[242,5445,"kushal","hello","hi",[5,3,5,54]]
# for i in range(len(lst)):
#     if type(lst[i])==list:
#         print("Consider sublist")
        

#Question 9:
# lst=[5,82,6.5,1,5,6,7,9,8]
# lst.sort()
# print(lst[1])

#Question 10:
# lst=[10,20,42,10,22,39,42]

# uniquelst=[]
# for i in lst:
#     if i not in uniquelst:
#         uniquelst.append(i)

# print(uniquelst)


#Question 11:

# lst = [(1, 'a'), (2, 'b'), (3, 'c')]

# num, char = zip(*lst)

# print(list(num))
# print(list(char))

#Question 12:

# lst = [(1,55), (2,10), (3,11),(4,50)]
# dict={}
# for i in lst:
#     dict[i[0]]=i[1]


#Question 13:
# d = {
#     "a": 5,
#     "b": 2,
#     "c": 8,
#     "d": 1
# }    
# sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
# values=dict.items(sorted_dict)
# print(values)


#Question 14:
# d = {
#     "a": 55,
#     "b": 92,
#     "c": 85,
#     "d": 10,
#     "e": 155,
#     "f":78
# }    
# sorted_dict=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
# print(sorted_dict)
# # values=sorted_dict.values() #Won't give access by index
# values=list(sorted_dict.values())
# print(values)
# print(f"Highest Value: {values[0]}")
# print(f"Second Highest Value: {values[1]}")
# print(f"Third Highest Value: {values[2]}")


#Question 15:
# n=int(input("Enter the number: "))
# a=0
# b=1

# for i in range(n):
#     print(a,end=" ")
    
#     # c=a+b
#     # a=b
#     # b=c
#     a,b=b,a+b


#Question 16:
# a=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
# d={}
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# d=dict(sorted(d.items()))
# print(d)


#Question 17:
# import math


# def oddseries(n):
#     numer=12
#     sum=0
#     for i in range(1,n+1,2):
#         temp=numer/math.factorial(i)
#         numer+=20
#         sum+=temp
#     return sum

# def evenseries(n):
#     numer=22
#     sum=0
#     for i in range(2,n+1,2):
#         temp=numer/math.factorial(i)
#         numer+=20
#         sum+=temp
#     return sum

# inp=int(input("Enter your number: "))
# oddseriesSum=oddseries(inp)
# evenseriesSum=evenseries(inp)
# print(f"Total sum: {oddseriesSum+evenseriesSum:.2f}")


#Question 18:
# def factorial(n):
#     if n==0 or n==1:
#         return 1
    
#     return n*factorial(n-1)

# inp=int(input("Enter the number: "))
# result=factorial(inp)
# print(f"Factorial: {result}")


#Question 19:
# a=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
# unique_lst=[]
# for i in a:
#     if i not in unique_lst:
#         unique_lst.append(i)
# print(unique_lst)



#Question 20:
import random
import string



class User:
    userid=1

    def __init__(self, name):
        self.id = User.userid
        self.name = name
        self.password=""
        User.userid += 1

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Password:", self.password)

    def generate_password(self,words):
        # specials=['@','#','$','!','*']
        try:
            specials="@$*%#!"
            password=""

            #Some random capital letter
            for ch in words:
                if random.choice([True,False]):
                    password+=ch.upper()
                else:
                    password+=ch.lower()

            # Ensure at least:
            # 1 digit
            # 1 special character
            # 1 capital letter

            password += random.choice(string.digits)
            password += random.choice(specials)
            password += random.choice(string.ascii_uppercase)

            all_chars=string.ascii_letters+string.digits+specials
            length=15
            while len(password)<length:
                password+=random.choice(all_chars)
            password=list(password)
            password=password[:15]
            random.shuffle(password)
            password="".join(password)
            self.password=password
            print(f"Genereted Password: {password}")
        except Exception as e:
            print(f"Error while generating password: {e}")

temp=[]
while True:
    try:
        name=input("Enter name or stop: ").strip()
        # Empty name check
        if not name:
            raise ValueError("Name cannot be empty")
        
        if name.lower()=="stop":
            break
        obj=User(name.lower())
        obj.generate_password(input("Enter the words for password (max 15 words): "))
        temp.append(obj)

    except ValueError as v:
        print(f"Value error: {v}")

    except Exception as e:
        print("Unexpected Error:", e)


users=tuple(temp)
print(f"Total Users: {User.userid-1}")
print("User Details: \n")

for obj in users:
    obj.display()
    print()