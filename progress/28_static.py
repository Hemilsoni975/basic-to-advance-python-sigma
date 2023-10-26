# static method is used when user doesn't want instance of class
# they are used as `@staticmethod` decorator and do not have access to instance of class that is "self"
# static method are used to make user code presize
# It is not necessary to call static method on instance variable
print("----------SIMPLE STATIC METHOD-----------")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printInfo(self):
        print(f"name : {self.name}\nsalary : {self.salary}")

    @staticmethod
    def print(a):
        print("I AM " + a)


e = Employee("hemil", 50000)
e.printInfo()
e.print("DEVELOPER")


class Maths:

    def __init__(self, num):
        self.num = num

    def calc(self, n ):
        self.num = self.num + n

    @staticmethod  # it helps function to display the output without using self arguement
    def add(a,b):
        return a + b

m = Maths(5)
print(m.num)
m.calc(10)
print(m.num)

print(m.add(3,4))