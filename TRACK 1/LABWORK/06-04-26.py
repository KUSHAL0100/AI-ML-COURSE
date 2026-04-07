"""#DATA STRUCTURES
#LIST
a=[10,30,50.6,10,10] #Mutable(Can edit Data Later on),Can contain duplicates,Heterogeneous(Contains any type of Data)
print(a[-1]) #It prints , print func and none both
print(a[::]) #Slice Way to print whole list

 
for i in range(len(a)): print(a[i])
for i in a: print(i)
print("\n\n\n")
 #Not work if it will have so many type of datatype withing same list,like characters,numbers,then it is not possible for calculations
print(len(a))
print(max(a))
print(min(a))

#Methods

a.append(500) #Will add element at the end
a.insert(2,1515) #Tell the index where you want to insert the element,and then enter the element 
print(a)

print(a.count(10)) #Will count how many times element occured in the list

print(a.index(10)) #First Occ of the element

a.remove(30) #Removes the First Occ of the element,But can't store in any variable
print(a)

print("Item will pop is: ",a[3])
popped_item=a.pop(3) #Can remove the element based on it's index,and before pop,Allowes to store that element value in any variable
print(popped_item)

print("The 0th index value Before Reverse is: ",a[0])
a.reverse() #Reverses Current List 
print(a)
print("The 0th index value after Reverse is: ",a[0])

a.sort() #Sorts list on ascending order
print(a)

new_lst=a.copy() #Creates Duplicate copy,and both copies are different,means it's an shallow_copy

print(new_lst)
new_lst.clear() #Clears All elements of the list
print(new_lst)
print(a)

#positive-negative
lst=[10,-50,-90,66,-88,754,694]
positive_lst=[]
negative_lst=[]
for i in lst:
    if i >=0: positive_lst.append(i)
    else: negative_lst.append(i)

print(f"Positive Elements Are: {positive_lst} \nNegative Elements Are: {negative_lst}")

#Mean element
sum=0
for i in lst: sum+=i
print(f"Mean element is: {sum//len(lst)}")

lst=[10,-50,-90,66,-88,754,694]
max_element=max(lst)
print(f"Max Element is: {max_element} with index: {lst.index(max_element)}")

#ORR
max_element=0
max_element_index=None
for i in range(len(lst)):
    if lst[i]>max_element: 
        max_element=lst[i]
        max_element_index=i
print(f"Max Element is: {max_element} with index: {max_element_index}")

#ORR
lst=[10,-50,-90,66,-88,754,694]
lst.sort()
print(f"Second Gretest Element : {lst[-1]} with the index {len(lst)-2}") #-2 etle kem ke length 1 thi start thay ganvani and for index 0 start thay,ne 1 number pachad javanu for  largest element
#SECOND greatest element
print(f"Second Gretest Element : {lst[-2]} with the index {len(lst)-3}") #-3 etle kem ke length 1 thi start thay ganvani and for index 0 start thay,ne 2 number pachad javanu for second largest element

#ORR
lst=[10,-50,-90,66,-88,754,694]
largest=lst[0]
second_largest=lst[0]
for i in lst:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest:second_largest=i

print(second_largest)

#Check if list is sorted or not
lst.sort()
for i in range(len(lst)-1):
    if lst[i] >lst[i+1]: 
        print("List is not sorted")
        break
else: print("List is sorted")


#TUPLES
#Only diff between list and tuples are,mutability
#List are mutable,you can change values using index any time,whereas tuples are immutable,you can't channge values,certainly you can insert and delete but can't moodify,they are like strings,both share same functionalities in terms of accessing

#Tuples are used less,only two three methods like index,count etc
tpl=10,15,30,50,20 #This will also create tuples
print(tpl)
tpl=(44,50,99,44,85,44) #This is the Standard Way
print(tpl)
print(tpl.index(44)) #Will return first occurance index of the value

print(tpl.count(44)) #How many times element occured

#SETS
#SETS are mutable,can't contain duplicate values,can't be accessed thorugh  index cause they are unordered,doesn't mean that you entered 1,2,3 so it will store it like 1,2,3 , and it can't store all types of data,some are allowed like string,numbers,tuples etc

#Each value in a set is hashed using a hash function (hash() in Python). The hash is used as an index to store the element in memory OF Since hashing does not maintain order, sets are unordered. Only immutable (hashable) objects can be stored in a set (e.g., numbers, strings, tuples). Mutable objects like lists and dictionaries are not allowed.

#A set cannot be traversed using the index values cause it is unordered and has no index.
#Numbers are also immutable in python
x=5
x+=1

#Here python doesn't updates it's value,instead it re-calculates 5+1=6 and then reallocates new value's reference to X,instead of changing it

#So immutable objects are allowed in sets (numbers,string,tuples)
#Sets stores value in hash format
#How hash work? see
a=hash("Helloooo") #Everytime hash will have diff value
print(a)
a=hash((10,20,888,69))
print(a)

#Sets stores hash values randomly
a={1,8,7,66,2,5,"hello",55,"kushal",61}
print(a) #Here you'll see it will not print in the same order

for i in a: print(i) #You can access Sets this way too

#Sets has methods for mutability
a={1,2,3,4,5}
b={4,5,6,7,8}

a.add(6) #Adds an element to the set
print(a)
a.remove(6) #Removes element ,and if not found returns an error
print(a)
a.discard(6) #Removes element,and if not found does not return an error
print(a)
a.pop() #Removes Random Element from the set
print(a)
ele=a.pop() #Can store value before removing
print(ele)
print(a)
a={1,2,3,4,5}
b={4,5,6,7,8}
#union, shortcut | , removes duplicate, can be used as compund operation, e.g a=10,b=20, a+=b, ans a=30
ans=a.union(b)
print(ans)
#a|=b #Instead of storing union in another variable,you can do it on current one to,same compund for every operation like, intersection,differentiation etc 
# print(a)

#Intersection, shortcut &, extracts common elements
ans=a.intersection(b)
print(ans) 

# ans=a&b
# a&=b

#Difference, shortcut -, removes common element from one set,with coparing second one
ans=a.difference(b)
print(ans)
ans=b.difference(a)
print(ans)

# ans=a-b
# a-=b

#Symmetric Diff, shortcut ^, removes common element from both the sent
ans=a.symmetric_difference(b)
# ans=a^b
# ans=b^a #Here both ment same,as it only removes common element from both set
# a^=b
print(ans)

#dictionaries
#Merging 2 dictionaries
d1={10:100,20:200,40:300}
d2={40:400,50:500,60:600}

for i in d2: #only i will give key,but i in that perticular variable will give value
    d1[i]=d2[i]
print(d1)

# for i in d2.values(): #This will give only values
#     print(i)


#Count the freq of each element in the list
a=[1,1,1,3,5,2,5,6,7,3,2,1,6,5,3,3]
d1={} #Empty Dictionary
# for i in a:
#     if d1.get(i): d1[i]+=1
#     else: d1[i]=1 ORRRRRRRRRRRRRR
for i in a:
    if i in d1.keys():d1[i]+=1
    else: d1[i]=1

print(d1)

#Add values of common keys 
d1={10:100,20:200,40:300}
d2={40:400,50:500,60:600}
for i in d1:
    if i in d2.keys(): d1[i]+=d2[i] 
    else:d1[i]=d2[i]
# for i in d2:
#     if i in d1.keys(): d1[i]+=d2[i]
    # else:d1[i]=d2[i]


print(d1)
"""


from pathlib import Path
import os
def readfileandfolder(): 
    try:
        path=Path('')
        items=list(path.rglob('*'))
        for i,items in enumerate(items):
            print(f"{i} :- {items} ")
    except Exception as err: print(f"The error occured as: {err}")

def createfile():
    try:
        readfileandfolder()
        name=input("Enter The File name: ")
        path=Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                content=input("What you want to write in this file: ")
                fs.write(content)
            print("File Created Sucessfully")
        else: print("File Already Exists")
    except Exception as err: print(f"The error occured as: {err}")

def readfile():
    try:
        readfileandfolder()
        name=input("Enter the file name you want to read: ")
        path=Path(name)

        if path.exists() and path.is_file():
            with open(path,"r") as fs:
                print(fs.read())
        else: print("Enter the appropriate file name")
    except Exception as err: print(f"The error occured as: {err}")


def updatefile():
    try:
        readfileandfolder()

        name=input("Enter Your File name: ")
        path=Path(name)

        if path.exists() and path.is_file():
            print("Press 1 for renaming file name")
            print("Press 2 for overwritting file")
            print("Press 3 for adding content in file")
            res=int(input("Enter Your Response: "))
            match res:
                case 1:
                    name2=input("Enter New name for the file: ")
                    path2=Path(name2)
                    path.rename(path2)
                case 2:
                    with open(path,"w") as fs:
                        content=input("Enter your content: ")
                        fs.write(content)
                case 3:
                    with open(path,"a") as fs:
                        content=input("Enter your content to append: ")
                        fs.write("\n"+content)
                case _:
                    print("Enter Appropriate Input")
        else: print("Enter Appropriate File Name")
    except Exception as err: print(f"The error occured as: {err}")
 
def deletefile():
    try:
        readfileandfolder()
        name=input("Enter File name You want to delete: ")
        path=Path(name)
        if path.exists() and path.is_file():
            os.remove(path)
            print("Your File deleted Sucessfully")
        else: print("Enter Appropriate File name")
    except Exception as err: print(f"The error occured as: {err}")



print("Press 1 to Create a file")
print("Press 2 to read a file")
print("Press 3 to Update a file")
print("Press 4 to delete a file")

res=int(input("Enter Your Response: "))
match res:
    case 1: createfile()
    case 2: readfile()
    case 3: updatefile()
    case 4: deletefile()
    case _: print("Enter Appropriate Response")