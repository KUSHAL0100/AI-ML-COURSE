#polymorphisam
"""
1.method overloading - not supported in python
2. method overriding- supported
"""


class My:
    def show(self):
        print("Method 1!!")
    
class My1:
    def show(self):
        super().show()
        print("Method 2!!")


#My2 thi My1 ma jase tya thi My ma jase,kmk bracket ma left to right jay vastuo
class My2(My1,My):
    def show(self):
        super().show()
        print("Method 3!!")


obj=My2()
obj.show()
    