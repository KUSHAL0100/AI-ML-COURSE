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

"""

year=int(input("Enter The year to check leap year or not: "))
print("Leap yea675r") if(year%400==0 or (year%100 !=0 and year %4==0)) else print("Not a Leap Year")