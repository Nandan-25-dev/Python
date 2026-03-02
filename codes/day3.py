class Parent:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Name: ",self.name)
class Child(Parent):
    def __init__(self,name,usn,marks):
        super().__init__(name)
        self.usn=usn
        self.marks=marks
    def tot(self):
        return sum(self.marks)
    def display(self):
        self.show()
        print("Usn -",self.usn)
        print("Marks - ",self.marks)
        print('Total -',self.tot())
s1=Child("Nandan","111",[98,92,90])
s2=Child("Random","92",[99,93,91])
s1.display()
s2.display()