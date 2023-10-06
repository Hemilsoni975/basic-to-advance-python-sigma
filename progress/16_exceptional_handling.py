'''
Exceptional handling is process of handling the unexpected or unwanted events on computer system
It deals with unwanted or unexpected event to avoid crashing of system and to avoid disruption

Types of error in exceptional handling :

A)  syntax error : cannot be handle by user

B)  Logical error : can be handle by user

    1) ZeroDivisionError   : raised when number is divisible by zero
    2) NameError           : raised when variable or funciton name is not found
    3) TypeError           : raised when you enter int value in place of string ,etc...
    4) ValueError          : raised when function or method is called with an invalid arguement or input
    5) IndexError          : raised when index is out of range
    6) KeyError            : raised when key is not present in that dictionary
    7) ModuleNotFoundError : raised when module user try to import is not found
    8) ImportError         : raised when you try to import module and that module is not found
    9) FloatingError       : raised when you enter int value in place of floating value
    10) MemoryError        : raised when program runs out of memory space
    11) IOError            : raised when I/O fails
    12) AttributeError     : rasied when any attribute or method is not found
Try : statements with can may generate exception
Catch : solution of exeption generated
Finally : it will execute whether exception is handled or not
raise : manually trigger when exception occured
'''

a = input("Enter the number : ")

print(f"Multiplication table of {a} is : ")
try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except Exception as e:
    print("Sorry! Invalid input")
print("END LINES")


def exception():

    try:
        a = [1, 2, 3, 4, 5]
        b = int(input("enter index : "))
        print(a[b])

    except:
        print("some error occured")

    finally:
        print("i will get always executed")

x = exception()
print(x)

try:
    i = int(input("enter number to check even_odd : "))

    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")
except:
    print("please enter only number")
finally:
    print("you were good to us")

def election():
    age = int(input("Enter your age to check you are eligible or not for voting : "))
    try:
        if age >=18 :
            print("You are eligible for voting")
        else:
            print("you are not eligible for voting")
    except ValueError:
        print("invalid input")
    finally:
        print("vote as per your observation")
x = election()
print(x)

print("------RAISE-CUSTOM-ERROR------")

a = int(input("Enter number between 1 to 20 : "))

if (a<1 or a>20):
    raise ValueError("please enter between 1 to 20")
else:
    print(a)
