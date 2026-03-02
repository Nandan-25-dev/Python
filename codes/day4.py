#In this pgm same funcn but is being overridden hence its called as polymorphism, same command but diff outputs i.e, polymorphism
class Person:
    def role(self):
        print("I am a person")
    def job(self):
        print("I give peron details")
class student(Person):
    def role(self):
        print("Im a student")
    def job(self):
        print("I give student details")
class teacher(Person):
    def role(self):
        print("Im a teacher")
    def job(self):
        print("I give teacher details")
People=[Person(),student(),teacher()]
for p in (People):
    p.role()
    p.job()
    print() #Only used to print in next line after each loop