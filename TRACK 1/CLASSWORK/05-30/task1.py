#OOPS INHERITANCE
#Inheritance means one class derive properties of anohter class
#It has 5 types
'''
1.single
2.mutilevel
3.multiple
4.hierarchy
5.hybrid
'''

# 1.single
class A:
    def fun1(self):
        print("Method 1!!")

class B(A):
    def fun2(self):
        print("Method 2!!!")


#Multilevel
class C(B):
    def fun3(self):
        print("Method 3!!!")
obj=C()
obj.fun1()
obj.fun2()
obj.fun3()


#Multiple, a to b,a to c
class Vehicle:
    def show(self):
        print("I am vehicle")

class Truck():
    def show2(self):
        print("I am truck")

class Car(Vehicle,Truck):
    def show3(self):
        print("I am car")
    


#Hierarchy
# a to b and c  

class X:
    def show(self):
        print("Hello i am from x")


class Y(X):
    def show2(self):
        print("I am from class y")

class Z(X):
    def show3(self):
        print("I am from class Z")

obj1=Y()
obj1.show()
obj1.show2()

obj2=Z()
obj2.show()
obj2.show3()




#Hyrbid(Genrally single+multiple)

class User:
    def show(self):
        print("I am user")


class Student(User):
    def show2(self):
        print("I am Student")

class Teacher:
    def show3(self):
        print("I am Teacher")

class Principle(Student,Teacher):
    def show4(self):
        print("I handle everything!!!")

