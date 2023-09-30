a = int(input("enter value of a : ")) # taking values form user
b = int(input("enter value of b : "))
c = int(input("enter value of c : "))
d = int(input("enter value of d : "))


# using only if statement
if c != d:
    print("true")


# simple if and else
if a % 2 == 0:
    print(a, "is even")
else:
    print(a, "is odd")

# if_elif_else statement
if a > b and a > c:
    print(a, "is greater")
elif b > c:
    print(b, "is greater")
else:
    print(c, "is greater")

# using if statement in list
mylist = [2, 4, 5, 7, 8, 9]
print(4 in mylist)
if 3 not in mylist:
    print(False)


# nested if statement
print("blood donation camp")
age = int(input("Enter age:- "))
wieght = int(input("Enter wieght:- "))

if age >= 18 and age <=55:
    if wieght > 45:
        print("Congratulations!!! You are eligible for blood donation")
    else:
        print("sorry!!! your wieght is not enough")
else:
    print("sorry!!! your age is not enough")