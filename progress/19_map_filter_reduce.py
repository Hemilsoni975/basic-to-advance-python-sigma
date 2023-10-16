# map , filter , and reduce are higher order functions that takes another functions as arguements.
#
# map fucntion is used for type  conversion that makes code of onyl one line
print("------------------MAP_FUNCTION------------------")
n = []
u = int(input("Enter how many element : "))
for i in range(u):
    a = input("Enter no : ")
    n.append(a)
print(n)

# for j in range(len(n)):   # everytime for converting string to int in list if you don't want for loop use map() function
#     n[j] = int(n[j])

n = list(map(int, n))
n[2] = n[2] + 5
print(n[2])


n = []
u = int(input("Enter how many element you want in list : "))
for i in range(u):
    a = input("Enter no : ")
    n.append(a)
print(n)
n = list(map(int, n))
square = list(map(lambda m: m * m, n))
print("Square of list : ", square)

n = []
user = int(input("Enter how many element : "))
for i in range(user):
    a = int(input("Enter no : "))
    n.append(a)
print(n)

def square(x):
    return x * x

def cube(x):
    return x * x * x

func = [square, cube]

for j in n:
    val = list(map(lambda x: x(j), func))
    print(val)

print("------------------FILTER_FUNCTION------------------")

# The filter functions are used for qualifying values from the list which will return true
n = []
user = int(input("Enter how many element to insert : "))
for i in range(user):
    a = int(input("Enter no : "))
    n.append(a)
print(n)
g = list(filter(lambda x : x > 5, n))
print(g)

print("------------------REDUCE_FUNCTION------------------")
# reduce functions helps to perform simple operations

from functools import reduce
n = []
user = int(input("Enter how many element to insert : "))
for i in range(user):
    a = int(input("Enter no : "))
    n.append(a)
print(n)

# m = 0   # if user want short code of this operation he can simple use reduce keyword
# for i in n:
#     m = m + i
# print(m)

val = reduce(lambda x,y:x+y, n)
print(val)

val = reduce(lambda x,y:x*y, n)
print(val)
