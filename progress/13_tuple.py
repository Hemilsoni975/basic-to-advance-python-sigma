# Tuple is immutable means it cannot be change

a = (1)
b = (1,)
print("a is", type(a))
print("b is", type(b))

print("-----+++++-----")

wow = (20, 20, 30, 40, 50, "hemil", "umang")

print(wow)
print(wow[6])
print(wow[-2])

print("-----+++++-----")

if "hemil" in wow:
    print("heyy!!!")

print("-----+++++-----")

wow1 = wow[1:5]
print(len(wow1))

print("-----METHODS OF TUPLE-----")

#  method of inserting element in tuple
wow2 = list(wow)
wow2[2] = "kesar"
wow = tuple(wow2)
print(wow)

#find length of tuple
print(len(wow))

# count method
ok = wow.count(20)
print(ok)

# index method
ok =wow.index(50)
print(ok)

del wow  # helps to delete whole tuple
