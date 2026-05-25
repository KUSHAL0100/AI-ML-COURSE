
import random

# l=[34343,43546,231315,464523425,4e324232]

# print(random.choice(l))

lucky=random.randint(1,51)

print("***********Random number between 1 to 50")
# while True:
#     num=int(input("Enter your choice: "))
#     if num<1 or num>50:
#         print("Invalid Number!!")
#         break
#     elif num==lucky:
#         print("You have Won!!")
#         break
#     elif num>lucky:
#         print("Number is smaller!!")
#     else:
#         print("Num is bigger!!")
flag=0
for i in range(1,5):
    num=int(input("Enter your choice: "))
    if num<1 or num>50:
        print("Invalid Number!!")
        flag+=1
        break
    elif num==lucky:
        print("You have Won!!")
        flag+=1
        break
    elif num>lucky:
        print("Number is smaller!!")
    else:
        print("Num is bigger!!")

if flag==0:
    print("You have lost!!!")