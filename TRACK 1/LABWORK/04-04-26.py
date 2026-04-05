 #LOGICAL OPERATORS

a=100>150,34==34
print(a)
if not a:print("FALSEEE")
if a:print("TRUEEEE")



#remember in a, therre is 2 value,false and true,but it created ann tuple (will cover ahead) and stored those value these,and now tuple is not empty that's why it shows truee, even though it holds one falsy value

#SO how can i make a variable like,if he has any falsy value,then consider that variable a falsy one
#Answer is logical operator
a=100>150 and 36==36
print(a)
print("After logical operator")
if not a:print("FALSEEE")
if a:print("TRUEEEE")


#see how it printed false,and you already know logical operators like [and,or,not]
#and means,both condition must be true for getting true 
#or means either one condition true is enough
#not means,change the outcome
a=not 150>100 
print(a)
#here even though 150 is greater than 100 ,it printed false as not Will change the True to False and False to True

"""a=int(input("Enter The First Number: "))
b=int(input("Enter The Second Number: "))
print(f"{a} is Greater Than {b}") if(a>b) else print(f"{b} is Greater Than {a}")

#if(a>b):
#    print(f"{a} is Grater Than {b}")
#else:
#    print(f"{b} is Greater Than {a}")

#    "This is Traditional way"


name=input("What is your name: ")
gender=input("What is Your Gender: ")

#print(f"Good Morning {name} sir") if gender=="male" or gender=="m" else print(f"Good Morning {name} Ma'am") if gender=="female" or gender=="f" else print("Other")

#print(f"Good Morning {name} sir") if gender in ["male","m"] else print(f"Good Morning {name} Ma'am") if gender in ["female","f"] else print("Other")

#More improvement by making it case insensitive

print(f"Good Morning {name} sir") if gender.lower() in ["male","m"] else print(f"Good Morning {name} Ma'am") if gender.lower() in ["female","f"] else print("Other")

a=int(input("Enter The Number: "))
print("It is even number") if a%2==0 else print("It is an odd number")

name=input("What is your name: ")
age=int(input("Enter Your Age: "))
print("Valid Voter") if age>18 else print("Invalid Voter")


year=int(input("Enter The year to check leap year or not: "))
print("Leap year") if(year%400==0 or (year%100 !=0 and year %4==0)) else print("Not a Leap Year")

#TEMPRATUREEEEEEE
temp=int(input("Enter the Tempreture of your area: "))
if temp<=0:
    print("It is Very Freezing")
elif 0<temp<=10:
    print("It is very cold")
elif 10<temp<=20:
    print("It is cold")
elif 20<temp<=30:
    print("It is Pleasent")
elif 30<temp<=40:
    print("It is Hot")
elif temp>40:
    print("It is Very Hot")

#LOOPS
for i in range(1,6):
    print(i)
print("\n\n")
#  range(start,stop,steps), start and step is optional,bydefault start will be 0 and step will be 1
for i in range(6):
    print(i)

print("\n\n")
name="kushal"
for i in range(len(name)):
    print(name[i])

print("\n\n")
for char in name: #this method is simpler,but you don't have control on indexing anymore,works good for direct printing or iteration without operation
    print(char)

#Reverse for loop
n=int(input("Enter the Number: "))
for i in range(n,0,-1): print(i)
#table
n=int(input("Enter the Number: "))
for i in range(1,11):print(f"{n} * {i} = {n*i}")

#Sum upto N terms
n=int(input("Enter the Terms: "))
#sum=0
f#or i in range(n): sum+=(i+1)
#print(f"Sum is: {sum}")

sum=0
#OPTIONAL WAY FOR SUM
for i in range(1,n+1): sum+=(i)
print(f"Sum is: {sum}")


n=int(input("Enter the Fectorial: "))
factor=1
for i in range(n,0,-1): factor*=i
print(factor)
#SUM OF EVEN AND ODD NUMBERS SEPERETLY
n=int(input("Enter the Terms: "))
even=0
odd=0
for i in range(n+1):
    print(i)
    if i%2==0: even+=i
    else: odd+=i
print(f"Even Sum is: {even}, odd Sum is: {odd}")


#ALL FACTORS OF A NUMBER

n=int(input("Enter the Number to find out Factors: "))
for i in range(1,n):
    if(n%i==0):print(f"{i} is the factor of {n}")

#PERFECT NUMBER OR NOT(6=1,2,3),496,8128

n=int(input("Enter the Number to find out it is perfect number or not: "))
sum=0
for i in range(1,n):
    if(n%i==0):sum+=i

if(sum==n): print(f"Number {n} is a perfect Number")
else: print(f"Number {n} is not a perfect Number ")

n=int(input("Enter the Number to find out it is prime or not: "))
flag=0
for i in range(1,n+1):
    if(n%i==0):flag+=1

print("Number is prime") if(flag==2) else print("Number is not Prime")


n=int(input("Enter the Number "))
for i in range(n+1): print(i)

"""