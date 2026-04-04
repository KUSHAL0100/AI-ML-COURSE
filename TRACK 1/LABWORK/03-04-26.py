print("hello") 
a=02j
print(type(a))

b="j"
print(ord(b))

print(chr(106))


st="hi hello"
print(st[1])
print(st[-1])
#in slice [start step:end step:increase steps]
print(st[3:999:1])
print(st[3::1])
print(st[3::])
print(st[::])
# interpreter decoded= pehla a=complex hatu hve a ma int value to ee class int apse
a=5
print(type(a))

# EXPLICIT TYPE CONVERSTION(MANUAL)
a=str(a)
print(type(a))
print(a)

a=bool(a)
print(a)




# Falsy values and truthy values logic
bl=bool(0)
print("bl: ",bl)
bl=bool(500)
print("bl: ",bl)
bl=bool("")
print("bl: ",bl)

#so there are total 7 falsy values rest are truthy
#False , 0 , 0.0 , "" , [] , () , {}


#IMPLICIT TYPE CONVERSTION(PYTHON AUTOMATIC CONVERTS)
val=10
print(val/2) 
print(type(val/2)) #here it shows 5.0 ,it is implicit converstion



#FORMATED STRINGS
name="kushal"
age=20
print("Hello!! my name is ",name," And my age is  ",age," Yours?") #This is normal way of doing things
print(f"Hello!! My name is {name} And my age is {age} Yours??") #This is called formated string ,instead of creating multiple string use f at start and then do any type of calculation or use variable in {}, similar like $ and `` in javascript

#LET"S DO SOME EXPERIMENTS ON INPUT FUNCTION

"""name=input("Enter your name: ")
#age=input("Enter your age ") WRONG WAY TO STORE INT VALUES
age=int(input("Enter your age: "))

print(name)
#print(age+1) #You'll get error ,that python stores input bydefault in string format,so use explicit type conversion to store in int format
print(age+1)"""



#OPERATORSSSSSSSS
a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a%b) #reminder je niche vadhse ee,it's a MOD operation
print(a/b) #ahi akhu bhagfal avse with point
print(a//b) #10/3 karya pachi je integer bhagfal hase ee avse ,it is call FLOOR DIVISION ,you know floor right,converts float into int
print(a**b) #10 to the power 3(10*10*10)

#python follows BODMAS (BHAGUSABA) /,*,+,-
print(12+4/2) #pehla bhagakar,then gunakar,then sarvado,then badbaki


#assignment operators
a=10
b=5
print(f"a: {a} and b: {b}")
b+=5 #same as b=b+5
print(b)
b+=a #it is same as , b=a+b
print(b)

#other assignment operators b+=, b-=, b*=, b/=, b//=, b%=, b**=



#comparison operations <, >, <=, >=, ==, !=
if(a>b): print("a is greater")  
else: print("b is greater")

print("ABC" >"BCD") #ALLOWED , O/P WILL BE FALSE
print("A"<="B") #ALLOWED
#print("A" >= 65) #NOT ALLOWED

#One liner if else
b=21
print("B is greater than 20") if(b>20) else print("B is smaller than 20")


#c=100 if b<20 else c=50 ERORRRRR
c=100 if b<20 else 50

print(c)

x=0
result = "Positive" if x > 0 else "Negative" if x < 0 else "Zero" 
"""
Breakdown
x>0 print positive
else if
x<0 print negative
else zero
"""
print(result)

"""Refer 4th april file"""