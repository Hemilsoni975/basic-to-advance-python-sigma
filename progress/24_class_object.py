# class is like a template
# class is blueprint for creating  objects
# keyword = "class class_name"
# object is instance variable of class
# self parameter is referref to current instance of the class, and is used to access variable belongs to class

print("------------------simple-calc-------------------")


class math:
    def value(self,x,y):
        self.x = x
        self.y = y

    def add(self, x, y):
        print("value : ", x+y)
    def sub(self, x, y):
        print("value : ", x-y)

    def mul(self, x, y):
        print("value : ", x*y)

    def div(self, x, y):
        print("value : ", x/y)


# instance method of class
m = math()
m.add(3, 4)
m.sub(3, 4)
m.mul(3, 4)
m.div(3, 4)
print("------------------student-------------------")

class Student: # creating a class
    pass

hemil = Student() # instance variable - created object of class
hemil.name = "Hemil"
hemil.std = 3
hemil.sec = "D"
hemil.subject = ["CS", "Ml"]

print(hemil)
print(hemil.name)
print(hemil.std)
print(hemil.sec)
print(hemil.subject)


print("------------------employee------------------")

class Employee:
    no_of_leave = 6

hemil = Employee()
umang = Employee()

hemil.name = "Hemil"
hemil.profile = "python"

umang.name = "uma"
umang.profile = "front-end"

print(hemil.name)
print(hemil.profile)
hemil.no_of_leave = 10
print(hemil.no_of_leave)

print(umang.name)
print(umang.profile)
print(umang.no_of_leave)


print("------------------person-------------------")

class person:
    name = "hemil"
    age = 29
    occupation = "developer"

a = person()
print(a.name, a.age, a.occupation)

a.name = "mit"
a.occupation = "tester"
print(a.name, a.occupation)


print("------------------railway-------------------")
class Railway:
    def info(self): #self parameter is used to class curent object of class
        self.name = input("Enter name of visitor : ")
        self.age = int(input("Please enter you age : "))
        self.contact = int(input("Enter mobile number :"))



    def getData(self):
        print(f"The name of visitor is {self.name} and the age is {self.age} and contact details are {self.contact}")

r = Railway()
r.info()
r.getData()


print("------------------classmethod-------------------")
class company:
    company = "bmw"
    def bmw(self):
        print(f"the company is {self.company}")

    @classmethod # this  helps us to change directly the class only
    def change(jag, new):
        jag.company = new


c = company()
c.bmw()
c.change("jaguar")
c.bmw()
print(company.company)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

e = Employee("hemil", 25000)
print(e.name)
print(e.salary)

string = "mit-15000"
e1 = Employee.fromstr(string)
print(e1.name)
print(e1.salary)


print("------------------staticmethod-------------------")

class Math:

    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num+n

    @staticmethod
    def add(x,y):
        return x + y
m = Math(5)
print(m.num)
m.addtonum(10)
print(m.num)
# to print staticmethod syntax :- classname.function_name(values or parameters)
print(Math.add(10, 10))
