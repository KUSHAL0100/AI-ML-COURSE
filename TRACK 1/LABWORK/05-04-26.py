"""str="kushal"
#print(str[::-1]) built-in or medium built in method
#using for loop
for i in range(len(str)-1,-1,-1):
    print(str[i])
str=input("Enter the String: ").lower()
#don't do this,although it is write still
#rstr=str[::-1]
#if(str==rstr): print("Palindrome")
rstr=""
for i in range(len(str)-1,-1,-1):
    rstr+=str[i]

if(str==rstr): print("Palindrome")


#FUNCTIONS
def hello(name): #Parameters
    print(f"Hello {name}")

hello("kushal") #Arguments
hello(5)
hello("Rita")


def sum(num1,num2): print(f"{num1} is your First Number, {num2} is Second Number, Sum is: {num1+num2}")
sum(5,55)
sum(55,98)
sum(66,23)
sum(num2=550,num1=789) #Keyword Arguments
#sum(50) Not Allowed

def sub(num1,num2=100): return num1-num2

print(sub(150))

ans=sub(150,120)
print(ans)



"""