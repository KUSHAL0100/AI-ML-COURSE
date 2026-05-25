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
# # sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
# values=dict.items()



for i in range(6):
    for j in range(i+1):
        print(" *",end=" ")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print(" *",end=" ")
    print()