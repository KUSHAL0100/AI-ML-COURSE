# age=int(input("Enter the age:"))

# if (age>=100): print("Invalid age")
# elif(age>=18): print("Eligible to vote")
# else: print("Not eligible to vote")


# no1=int(input("enter the no.1: "))
# no2=int(input("Enter the no.2: "))

# if(no1>no2): print(f"{no1} is greater than {no2}")
# else: print(f"{no2} is greater than {no1}")


# print(f"{no1} is greater") if(no1>no2) else  print("Both are same") if(no1==no2) else print(f"{no2} is greater")
# n=int(input("Enter the number: "))
# print("Even!!!") if n%2==0 else print("Oddd!!!")

first_day=int(input("Enter first the day"))
first_month=int(input("Enter first the month: "))
first_year=int(input("Enter first the year: "))

second_day=int(input("Enter second the day: "))
second_month=int(input("Enter second the month: "))
second_year=int(input("Enter the second year: "))

if(second_year>2026):
    print("Enter valid date")
    

diffindays=second_day-first_day
diffinmonths=second_month-first_month
diffinyears=second_year-first_year

if diffindays <=0:
    if diffinmonths>1:
        diffinmonths-=1
        diffindays+=30
    elif diffinyears>=1:
        diffinmonths+=11
        diffinyears-=1
        diffindays+=30
        
elif diffinmonths<=0 and diffinyears>=1:
    diffinmonths+=12
    diffinyears-=1

print(f"Diff are: {diffinyears} year, {diffinmonths} month, {diffindays} days")
