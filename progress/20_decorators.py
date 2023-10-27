# => decorator is useful when user want same function to be in multiple functions
# => it is denoted by |"@function_name(arguement)"|
# => decorator are often used to add functionality to functions and methods, such logging , memoiztion and acccess control
# => decorator are used to modify the behaviour of the function or class.
# => In decorator, functions are used as parameter in another function and then call inside wrapper function
# decorators solve both issues:
# 1) code duplication
# 2) cluttering main logic of function with additional functionality

print("--------------Decorator without arguement----------------")


# decorator without arguement
def function1():
    print("heyy hemil")


func2 = function1
del function1
func2()

print("--------------Decorator with arguement----------------")


# decorator with arguement
def hey(hello):
    print("i am before hello function")
    hello()
    print("i am after hello function")


@hey
def hemil():
    print("hemil is best of best")


# hemil = hey(hemil)

def hii(hk):
    def soni(*args, **kwargs):
        # here '*args' means taking arguement as tuple
        # while '**kwargs' means taking arguement as dictionary in form of key-value
        print("good morning")
        hk(*args, **kwargs)
        print("thanks")

    return soni


@hii
def getdata():
    print("HEMIL SONI")


@hii
def add(x, y):
    print(x + y)


getdata()
add(3, 5)
# hii(add(4, 5))

print("------------------*args and **kwargs------------------")


def hello(*args, **kwargs):
    print("tuple :", args)
    print("dictionary :", kwargs)


hello("hemil", "mit", first="soni", mid="is always", last="the best")

print("------------------CHAINING_DECORATORS------------------")


# Chaining decorators means used of multiple decorators in one function
def maths(sq):
    def sq_inner():
        x = sq()
        return x * x

    return sq_inner


def multiply(wow):
    def mul_inner():
        x = wow()
        return 2 * x

    return mul_inner


@maths
@multiply
def calc():
    return 10


@multiply
@maths
def calc1():
    return 10


print(calc())
print(calc1())

import time


def time1(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " mil sec")
        return result

    return wrapper


@time1
def sq(n):
    result = []
    for number in n:
        result.append(number * number)
    return result


@time1
def cube(n):
    result = []
    for number in n:
        result.append(number * number * number)
    return result

array = range(1,10000)
s = sq(array)
c = cube(array)

