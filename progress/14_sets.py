# SET IS THE COLLECTIONS OF NON-REPEATATIVE SETS

     # Properties of sets :
     # --> sets are unordered
     # --> sets are unindexed means cannot access element by IndexError
     # --> no way to change items in set
     # --> do not contain duplicate values
from typing import Set

a = {2, 4, 5, 6, 4, 8}
print(a)

b = {19, "hemil", 4.5, True}
print(b)  # sets don't maintain the same order

c = set()  # helps to make empty set
print(type(b))

for value in b:
    print(value)



print()
print("----------------SETS-METHODS-----------------")
print()

print("-----UNION-METHODS-----")  # merge value in one set from both set

d = {"ahm", "mumbai", "delhi", "UP", "gir"}
e = {"ahm", "girnar", "lonavala", "gir"}
print("union : ", d.union(e))
d.update(e)
print("update : ", d)


print("--INTERSECTION-METHODS--")  # checks the common value of both set

f = {"ahm", "mumbai", "delhi", "UP", "gir"}
g = {"ahm", "girnar", "lonavala", "gir"}
f.intersection(g)
print("intersection :", f)
f.intersection_update(g)
print("intersection_update : ", f)

print("----SYMMETRIC-METHODS----")  # removes common values of both set

h = {"ahm", "mumbai", "delhi", "UP", "gir"}
i = {"ahm", "girnar", "lonavala", "gir"}
h.symmetric_difference(i)
print("symmetric_difference : ", h)
h.symmetric_difference_update(i)
print("symmetric_difference_update : ", h)

print("----DIFFERENCE METHOD----")  # remove common values from 1st set

j = {"ahm", "mumbai", "delhi", "UP", "gir"}
k = {"ahm", "girnar", "lonavala", "gir"}
j.difference(k)
print("difference : ", j)
j.difference_update(k)
print("difference_update : ", j)

print("------DISJOINT-SET------")  # don't have common values then true otherwise false

l = {"ahm", "mumbai", "delhi", "UP"}
m = {"girnar", "lonavala", "gir"}
n = {"gir"}
print("is_disjoint_set : ", l.isdisjoint(m))
print("is_disjoint_set : ", m.isdisjoint(n))

print("------SUPER-SETS------")  # one set contains all the value of main set

o = {"ahm", "mumbai", "delhi", "UP", "gir"}
p = {"ahm", "gir"}
q = {"ahm", "gir", "london"}
print("super_set", o.issuperset(p))
print("super_set", o.issuperset(q))

print("------SUB-SETS------")  # here main set is subset of one set which has all values

o = {"ahm", "mumbai", "delhi", "UP", "gir"}
p = {"ahm", "gir"}
q = {"ahm", "gir", "london"}
print("sub_set", p.issubset(o))
print("sub_set", q.issubset(o))

print("-----ADD-METHODS-----")  # help to add methods in set

o = {"ahm", "mumbai", "delhi", "UP", "gir"}
o.add("london")
print(o)

print("---REMOVE/DISCARD-MEHTODS---")  # helps to remove values from set

# difference between remove() and discard() is that if any value not present in set and still you are
# trying to remove that element then discard() will don't responses but remove() will throws an error.

o = {"ahm", "mumbai", "delhi", "UP", "gir"}
o.remove("UP")
print("to remove : ", o)
o.discard("delhi")
print("to discard : ", o)

print("------POP-MEHTODS------")   # remove random value from the set

o = {"ahm", "mumbai", "delhi", "UP", "gir"}
o.pop()
print(o)

print("------CLEAR-MEHTODS------")   # it makes set empty

o = {"ahm", "mumbai", "delhi", "UP", "gir"}
o.clear()
print(o)


print("--CHECK-IF-ITEM-EXIST--")

o = {"ahm", "mumbai", "delhi", "UP", "gir"}
if "ahm" in o:
    print(o, "yes present")
else:
    print(o, "no present")

print("----DELETE-MEHTODS----")   # it delete whole set

o = {"ahm", "mumbai", "delhi", "UP", "gir"}
del o
print(o)