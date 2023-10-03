# function is declare by "def()" keyword

# declaring and calling a funciton
def hey():
    print("hello world")

hey()

# function having arguement
def name(fname):
    print("Hello", fname)

name("Hemil")
name("Umang")
name("Aman")

# number of arguement
def wow(food,vehicle):
    print("i eat ",food,"in the ",vehicle)

wow("pizza","hondacity")

# arbitary arguement in the functions :- it means add "*" before arguement in function as to use that for many values
def child(*name):
    print("Reynold child is ", name[1])
    print("yem child is ", name[0])
child("yahoo", "flungflu")

# passing a list as an argument
def vehicle(cars):
    for i in cars:
        print("This",i,"is of Hemil Y. Soni")

car = ["JAGUAR", "BMW", "RANGE ROVER"]
vehicle(car)

# return values using return statement
def num(x):
    return x * 5

print(num(5))
print(num(10))
print(num(15))

# to pass the function without any values then write "pass" statement

# recursion function
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter number :"))
print(factorial(n))
