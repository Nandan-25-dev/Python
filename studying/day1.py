class Student:
    def __init__(self,name,usn,marks):
        self.name=name
        self.usn=usn
        self.marks=marks
    def tot(self):
        return sum(self.marks)
    def avg(self):
        return self.tot()/len(self.marks)
s1=Student("abc","123",[84,95,84])
print(s1.name,s1.usn,s1.marks,s1.tot(),s1.avg())
