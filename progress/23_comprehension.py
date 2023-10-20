# COMPREHENSION PROVIDE US WITH SHORT AND CONCISE WAY TO CONSTRUCT NEW SEQUENCE USING PREVIOUSLY DEFINED SEQUENCE

print("---------------LIST-COMPREHENSION---------------")
# LIST COMPREHENSION PROVIDES AN EASY AND SHORT SYNTAX TO CREATE A LIST


l = []

for i in range(100):
    if i % 3 == 0:
        l.append(i)
print(l)

# using list comprehension -

l = [i for i in range(100) if i % 3 == 0]
print(l)

# Generating Even and Odd list using List comprehensions

user = int(input("HOW MANY ?"))
l1 = [i for i in range(user) if i % 2 == 0]
print(l1, " are even")
l2 = [i for i in range(user) if i % 2 != 0]
print(l2, " are odd")

# Squaring Number using List comprehensions

user = int(input("Enter no. : "))
l = [i**2 for i in range(0, user+1)]
print(l)

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l)
l1 = [x for a in l for x in a]
print(l1)

print("------------DICTIONARY-COMPREHENSION------------")

dict1 = {i: f"value = {i}" for i in range(5)}
print(dict1)

l = [1, 2, 4, 5, 6]
myDict = {}
l1 = {i : i ** 3 for i in l if i % 2 != 0}
print(l1)

s = ['Gujarat', 'Maharashtra', 'Punjab']
c = ['Gandhinager', 'Mumbai', 'Chandigarh']

mydict = {f"key = {i}": f"value = {j}" for (i, j) in zip(s, c)}
print(mydict)



print("------------SET-COMPREHENSION------------")
# Set comprehension in Python is similar to list and dictionary comprehensions, but it is used to create sets.

s = {i for i in ["hemil", "umang", "tirth", "hemil", "umang", "tirth"]}
print(s)
print(type(s))

l = [1, 2, 3, 4, 5]
s = [i**2 for i in l]
print(s)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
s = {i for i in l if i % 2 == 0}
print(s," is even")

print("----------GENERATOR-COMPREHENSION----------")
# Generator Comprehensions are very similar to list comprehensions. One difference between them is
# that generator comprehensions use circular brackets whereas list comprehensions use square brackets.

g = (i for i in range(100) if i % 2 == 0)
print(g.__next__())  # it will return one value at  a time
print(g.__next__())  # it will return one value at  a time
print(g.__next__())  # it will return one value at  a time
print(g.__next__())  # it will return one value at  a time
print(g.__next__())  # it will return one value at  a time
print(g.__next__())  # it will return one value at  a time
print(g.__next__())  # it will return one value at  a time
print(g.__next__())  # it will return one value at  a time

# if you want all values to be print then let use loops

for j in g:
    print(j)

    