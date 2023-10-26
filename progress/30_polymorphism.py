# "polymorphishm" means "many forms"
# In programming it means same function name with different signature being used for different types.
# The key difference is data types and number of arguements used in function.

print("------------SIMPLE PROGRAM OF POLYMORPHISM--------------")

#  here "+" sign is performing both operations 1st addition and 2nd concatination
print("Addition : ", 10+20)
print("concatination: ", "10"+"20")

def add(x,y,z=0):
    return x + y + z


print(add(2,3))    # here 2 argument are given
print(add(2,3,4))   # here 3 arguement are given


print("---------------POLYMORPHISM USING CLASS-----------------")

class  person1:

    def method1(self):
        print("method 1 of person 1")

    def method2(self):
        print("method 2 of person 1")

class person2:

    def method1(self):
        print("method 1 of person 2")

    def method2(self):
        print("method 2 of person 2")

p1 = person1()
p2 = person2()

for p3 in (p1, p2):
    p3.method1()
    p3.method2()

print("-----------POLYMORPHISM USING INHERITANCE------------")

class parent:

    def par(self):
        print("HEY I AM PARENT CLASS METHOD")

class child1(parent):

    def child(self):
        print("HEY I AM CHILD1 CLASS METHOD")

class child2(parent):

    def child(self):
        print("HEY I AM CHILD2 CLASS METHOD")

person = [child1(),child2()]  # taking object as list

for persons in person:
    persons.child()

# In Python, polymorphism is typically achieved through method overriding and method overloading

# Types of polymorphism are :-
# 1) COMPILE-TIME POLYMORPHISM WHICH IS METHOD OVERLOADING
# --> METHOD OVERLOADING => SAME FUNCTION NAME WITH DIFFERENT NUMBER OF ARUGEMENTS

print("---------------------METHOD OVERLOADIND-----------------------")

# simple program of overloading

class addition:

    def op(self, *args):
        num = len(args)
        if num == 1:
            print(f"cube       : {args[0] ** 3}")
        elif num == 2:
            print(f"multiply   : {args[0] * args[1]}")
        elif num == 3:
            print(f"subtration : {args[0] - args[1] - args[2]}")
        elif num == 4:
            print(f"addition   : {args[0] + args[1] + args[2] + args[3]}")

a = addition()
a.op(3)
a.op(3, 4)
a.op(10, 2, 4)
a.op(10, 11, 12, 14)



# 2) RUN-TIME POLYMORPHISM WHICH IS METHOD OVERRIDING
# --> METHOD OVERRIDING => SAME FUNCTION NAME WITH SAME NUMBER OF ARGUEMENTS

print("-----------------METHOD OVERRIDING-------------------")

class person:

    def gra(self):
        print(f"i am base class")

class grand(person):

    def gra(self):
        print(f"hey")

class father(person):

    def gra(self):
        print(f"wow")

g = grand()
g.gra()
f = father()
f.gra()
