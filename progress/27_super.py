# super() keyword
#           ==> used to refer parent class.
#           ==> usually useful when class inherits multiple parent class and user can call one method from anyone
#               parent class
#           ==> user can easily inherit constructor using super()
#           ==> also return the object that represent parent class
#           ==> helps subclass to inherit the superclass

print("---------SIMPLE USE OF SUPER() KEYWORD----------")


class parent:

    def par(self):
        print("I am parent class method")


class child(parent):

    def child(self):
        print("I am child class method")
        super().par()  # using super() keyword we can easily inherit parent class in child class


c = child()
c.child()


class parent:

    def __init__(self):
        self.name = input("Enter name : ")
        self.roll = input("Enter roll : ")

    def par(self):
        print(f"Name : {self.name}\nRoll no. : {self.roll}")
        print("I am parent class method")


class child(parent):

    def par(self):
        print("hemil soni is best")
        super().par()

    def chi(self):
        print("I am child class method")
        super().par()


c = child()
c.par()
c.chi()

print("---------CONSTRUCTOR USING SUPER() KEYWORD----------")


#  USER CAN EASILY USE THE CONSTRUCTOR OF PARENT CLASS USING SUPER() KEYWORD

class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("I am parent class constructor")


class Programmer(Employee):

    def __init__(self, name, id, job):
        super().__init__(name, id)
        self.job = job
        print("I am inheriting parent class in child class")


p = Programmer("Hemil", 12, "python")
print(p.name)
print(p.id)
print(p.job)

q = Programmer("Mit",16,"bussiness developer")
print(q.name)
print(q.id)
print(q.job)

print("----------MULTIPLE INHERITANCE USING SUPER() KEYWORD-----------")


class father:
    def parent(self):
        print("I am the father_class")


class mother:
    def mparent(self):
        print("I am the mother_class")


class child(father,mother):
    def chi(self):
        super().parent()
        print("I am the child_class")
        super().mparent()

c = child()
c.chi()

print("----------MULTILEVEL INHERITANCE USING SUPER() KEYWORD-----------")

class grand:

    def gparent(self):
        print("I am grand class method 1 ")

class parent(grand):

    def pparent(self):
        print("I am parent class method inheriting grand")

class child(parent):

    def cparent(self):
        super().gparent()
        super().pparent()
        print("I am child class method inheriting both grand and parent ")

c =  child()
c.cparent()