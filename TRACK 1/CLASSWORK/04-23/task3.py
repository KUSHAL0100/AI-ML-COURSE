# #2) function with para without return type
# #3) function without para with return type

# #parameters

# #arguments 


# def fun1(n   ,a=0):
#     b=1
#     print(f"1: {a}")
#     print(f"2: {b}")
#     for i in range(3,n+1):
#         sum=a+b
#         a=b
#         b=sum
#         print(f"{i}: {b}")

# n1 = int(input("Enter Number : "))

# fun1(n1)    #arguments

# # print("Hello")
# # input()
# # range(2,11,4)


# a=10
# print(a)



def fun2():
    n1=10
    n2=20

    return n1+n2
# print(fun2())

result = fun2()
print(result)


def add(a,b):
    return a+b

n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))

res=add(n1,n2)
print(res)