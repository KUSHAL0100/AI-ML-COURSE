n1=int(input("Enter No1: "))
n2=int(input("Enter No2: "))
n3=int(input("Enter No3: "))
n4=int(input("Enter No4: "))

if n1>n2:
    if n1>n3:
        if n1>n4: print("N1 is Greater!!")
        else: print("N4 is greater!!")
    else:
        if n3>n4: print("N3 is greater")
        else: print("N4 is Greater!!")
elif n2>n3:
    if n2>n4:print("N2 is Greater!!")
    else: print("N4 is greater!!")
else:
    if n3>n4: print("N3 is Greater!!")
    else: print("N4 is Greater!!!")