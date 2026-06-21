#Encapsulation

"""
data binding into single entity it is call class

pointer
    stores the address of the next variable 

"""

class encaps:
    def show1(self):
        a=10
        self.a=a #Passes Reference
    def show2(self):
        # print(a) will throw an error
        print(self.a)

obj=encaps()
obj.show1()
obj.show2()