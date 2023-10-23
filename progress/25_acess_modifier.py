# There are 3 types of access modifier :
#     1) public : Access from outside the functions for class
#     2) private : Able to access in specific fucntion or class
#     3)protected : Member can be access within the class or subclasses


print("--------------PUBLIC---------------")
#  all the methods and variable are by default `public` in python.Any instance variable in class is followed by self
#  keword that is `self.var_name` are public accessed.

class Employee:
    def __init__(self):
        self.name = "hemil"

e = Employee()
print(e.name)

print("--------------PRIVATE---------------")
# private members of a class are those which can be accessed inside the class only. In python, there is no strict
# concept of `private` acess modifier. however the variable or members should consider private by prefixing its name '
# with double underscore(__).

class Employee:
    def __init__(self):
        self.__name = "hemil"

e = Employee()
# print(e.name) #  cannot be accessed directly
print(e._Employee__name) # can be access indirectly due to name mangling
print(e.__dir__())

# namemangling in python is technique used to protect class and superclass attribute


print("--------------PROTECTED---------------")
# protected is used to describe a member of a class that is intended to be accessed only by class itself and the
# subclasses. It is represented by single underscore `(_)`

class student:
    def __init__(self):
        self._name = "hemil"

        # PROTECT CLASS
    def _func(self):
        return "Hemil soni"

class marks(student):
    pass

obj = student()
obj1 = marks()
print(dir(obj))
print(obj._name)
print(obj._func())
print(obj1._name)
print(obj1._func())
