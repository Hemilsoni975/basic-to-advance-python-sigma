"""
Variable Naming Conventions:

Variable names can contain letters :-
    1) a-z
    2) A-Z
    3) digits (0-9)
    4) underscores (_)
    
Variable names must start with :-
    1) a-z
    2) A-Z
    3) underscore (_)
        
"""

# declaring variables 

x1 = "Hemil "     # declaring in double quotes
x2 = 'Hemil Y.'     # declaring in single quotes
x3 = '''Hemil Y. Soni''' # declaring in triple quotes

# case-sensitive

y = 5 
Y = "heyy!!!" 

# assigning multiple values in to multiple variable 
a, b, c, d = "My" , "name" , "is" , "name"

# adding of 2 variable
m = 5
n = 15

#global keyword
p = "Hello"

def ok():
    global p
    p = "Hy"
ok()
print(p +" Hemil")

print("-----------------------")

print(x1)
print(x2)
print(x3)

print("-----------------------")

print(y)
print(Y)

print("-----------------------")

print(a)
print(b)
print(c)
print(d)

print("-----------------------")

print(m+n)