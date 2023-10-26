# magic() is also called as dunder() methods
# they are special types of words
# magic methods are represented by "__" double underscore in front and back of keyword

print("-------------------len()----------------------")


# used to find length of the list or dictionary or the words
class Employee:
    name = "fowfdnsol"

    def __len__(self):
        c = 0
        for i in self.name:
            c = c + 1
        return c


e = Employee()
print(e.name)
print(len(e))

print("----------------init()-----------------------")


# init() method is a special method that is automatically invoked when you create innstance of class.
# it is also know as constructor of class

class Employee:

    def __init__(self, name):
        self.name = name

    def dis(self):
        print(f"my name is {self.name}")


e = Employee("Hemil Soni")
e.dis()

print("---------------str() and repr()-------------------")


# both the methods are used to convert an object into string representation.
# repr() and str() should compulsory have return statement
# the str() method is used to print object whereas repr() is used to when you want string representation of object that
# can help to recreate
class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"str {self.name}"

    def __repr__(self):
        return f"repr {self.name}"


e = Employee("Hemil soni")
print(str(e))
print(repr(e))

print("---------------call()-------------------")


class Employee:
    def __init__(self, name):
        self.name = name

    def dis(self):
        print(f"name is {self.name}")

    def __call__(self, *args, **kwargs):
        print("I am good person")


e = Employee("HEMIL")
e.dis()
e()

print("---------------add() and truediv()------------------")


class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID : {self.id}\nName : {self.name}\nSalary : {self.salary}")

    def __add__(self, other):
        return self.name + other.name

    def __truediv__(self, other):
        return self.salary / other.salary


e = Employee(1, "Hemil", 50000)
e.display()
f = Employee(2, "Mit", 100000)
f.display()
print(e + f)
print(e / f)

print("-------if __next__ == '__main__'--------")

# it is commonly used pattern in python to check whether the script is directly running or is imported as
# module in another script
# " __name__ " is the built-in variable that is automatically set to the name of current module.
# this idiom is very useful for code reuse-ability from a script by importing it as module in another script
class Employee:

    def printInfo(self):
        print("hey it's hemil here")

e =Employee()
print(__name__)
if __name__ == "__main__":
    e.printInfo()
