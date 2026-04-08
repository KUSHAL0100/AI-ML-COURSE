a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print(f"The value of a is: {a}, and the value of b is: {b}")

a=a+b
b=a-b
a=a-b
print(f"After swapping, the value of a is: {a}, and the value of b is: {b}")