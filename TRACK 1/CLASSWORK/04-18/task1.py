#patterns 

#right angel

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# print()
# for i in range(5):
#     print(i)
#     for j in range(i):
#         print(j,end="")
#         # print("*",end="")
#     print()

#Pyramid:

# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(" *",end="")
    # print()


#only supported in python
# for i in range(1,6):
#     print("*"*i)    


# for i in range(1,6):
#     print(" "*(6-i),"*"*i)


for i in range(1,6,1):
    print(" "*(6-i)," *"*i)

for i in range(5,0,-1):
    print(" "*(6-i)," *"*i)
  

# for i in range(1,6,1):
#     print("*"*i)