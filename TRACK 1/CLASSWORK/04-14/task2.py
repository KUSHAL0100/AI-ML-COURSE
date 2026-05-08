#Summition of number
# i=int(input("Enter your number: "))

# sum=0
# while i>=1:
#     sum+=i
#     i-=1
# print(f"Sum is: {sum}")


#Factorial of number
# n=int(input("Enter number to print the table: "))
# i=1
# while i<=10:
#     print(f"{n} * {i} = {n*i}")
#     i+=1

#fibonacci series
a=0
b=1

n=int(input("Enter the number: "))
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)
    # a,b=b,a+b