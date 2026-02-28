class Student:
    def __init__(self,name,usn,marks):
        self.name=name
        self.usn=usn
        self.marks=marks
    def tot(self):
        return sum(self.marks)
    def display(self):
        print("Name  - ",self.name)
        print("Usn   - ",self.usn)
        print("Marks - ",self.marks)
        print('Total -',self.tot())
s1=Student("nandan",111,[90,91,92])
s1.display()