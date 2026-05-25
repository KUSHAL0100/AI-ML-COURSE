#tuple

#Immutable,orderable,similar and non similar datatype
t=(1) #int
t=(1,) #tuple
t=(1,2,4,"Hello",True) #Tuple

#2 methods exissts in tuple
print(t.count(1)) #1 and True
print(t.index(2))



#Dictionaries
#Collection to store data in key and value pair
#key must be unique,mutable 

d={1:"Hello","kushal":2}

print(d)
print(d.get("kushal"))
print(d.items())
print(d.keys())
# print(d.pop("kushal"))
d.pop("kushal")
print(d)
# print(d.update({2:"hiii",3:"How are you"}))
d.update({2:"hiii",3:"How are you"})
print(d)
d.popitem()
print(d)
print(d.values())

t=(2,3,4)
d1={}
d1=d1.fromkeys(t) #Assigns keys with none,or given value to all
print(d1)

d2={}
for i in range(1,31):
    d2[i]=i*i #Key with value of it's square
print(d2)
