class User:
    def __init__(self,name):
        self.name=name

class Student(User):
    rollno=1
    def __init__(self, name):
        super().__init__(name)
        self.rollno=Student.rollno
        Student.rollno+=1

class Marks(Student):
    def __init__(self, name,marks):
        super().__init__(name)
        self.marks=marks

    def result(self):
        if self.marks>=80:
            print(f"{self.name} Got Distinction!!")
        elif self.marks>=60 and self.marks<80:
            print(f"{self.name} Got A Grade!!")
        elif self.marks>=40 and self.marks<60:
            print(f"{self.name} Got B Grade!!")
        elif self.marks<40:
            print(f"{self.name} Got C Grade!!")

s1=Marks("Kushal",79)
s2=Marks("Nirav",56)
s3=Marks("Rita",89)


s1.result()
s2.result()
s3.result()