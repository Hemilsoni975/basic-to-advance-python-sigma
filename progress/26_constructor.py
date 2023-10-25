# The constructor is a special methods used to create and initialize an object of class
# Constructor automatically called when object created.
# unique function that call automatically
# main aim is to initialize or assign values to data
# types of constructor :-
# 1) parameterized :- takes argument along with self
# 2) default :- only one argument that is self


print("---------------------------DEFAULT CONSTRUCTOR------------------------------")

print("--------------SELF---------------")


class Employee:

    def __init__(self, name, salary, job):
        self.name = name
        self.salary = salary
        self.job = job
        print(f"NAME:-{self.name}\nSALARY:-{self.salary}\nJOB PROFILE:-{self.job}")


emp1 = Employee("HEMIL", 50000, "PYTHON DEVELOPER")  # created a object of class

emp2 = Employee("MIT", 100000, "BUSSINESS DEVELOPER")


class animal:

    def __init__(self):
        print("DEFAULT CONSTRUCTOR")


a = animal()
b = animal()
print("-----------PARAMETERIZED CONSTRUCTOR-------------")


class person:

    def __init__(self, name, occ):
        print("PARAMETERIZED CONSTRUCTOR")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("hemil", "developer")
# b = person() # it will give error as 2 arguement is needed compulsory to call constructor
c = person("mit", "cheif")
a.info()
c.info()


print("-----------------DESTRUCTOR--------------------")
# destructor is used to delete unused objects
# the __del__() is used to call destructor

class animal:

    def __init__(self):
        print("constructor is created")

    def __del__(self):
        print("destructor is called")


e = animal()


class compare:

    def __init__(self):
        m = int(input("Enter no : "))
        n = int(input("Enter no : "))
        self.a = m
        self.b = n

    def max(self):
        if self.a < self.b:
            print(self.b, " is greater")
        else:
            print(self.a, " is greater")

    def __del__(self):
        print("destructor is called when function's does the operation")
c = compare()
c.max()

del c
# c.max() # it will throw an error as object "c" has been deleted
