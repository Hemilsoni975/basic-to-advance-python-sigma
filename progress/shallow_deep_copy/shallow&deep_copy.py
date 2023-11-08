#   changing in one can affect in another.
#   shallow copy is used when you want to store memory and when you want to change both list at same time.
#   shallow copy works as a assignment operator.
#   in shallow copy a new object is created and a new memory is also allocate in new list.
#   here if element in another list is changed then orignal list will also be affected.
#   Shallow copies are typically used when you need to create a quick copy of an object and you don't need to
#   modify the embedded objects.

import copy

print("============SHALLOW-COPY============")
mylist = [[1, 2, 3], [4, 5], [6, 'a']]
print("id of mylist : ", id(mylist))
print("id of mylist[0] : ", id(mylist[0]))
print("id of mylist[1] : ", id(mylist[1]))
print("id of mylist[2] : ", id(mylist[2]))

print('-'*35)
newlist = copy.copy(mylist)
print("id of mylist : ", id(newlist))
print("id of mylist[0] : ", id(newlist[0]))
print("id of mylist[1] : ", id(newlist[1]))
print("id of mylist[2] : ", id(newlist[2]))

#  here in shallow copy the id of both list are different but id of values in list is same

newlist[2][1] = 'HELLO'
print(mylist)
#  here you can see that changing values in newlist is also affected to original list.

print("============DEEP-COPY============")
#   in deep copy the different copies are made for nested elements
#   in deep copy if element in another list is change then the original list is unaffected.
#   deep copy is exact opposite of shallow copy.
#   Deep copies are typically used when you need to create a new object that is completely independent of the
#   original object, or when you need to modify the embedded objects without affecting the original object.

mylist = [[1, 2, 3], [4, 5], [6, 'a']]
print("id of mylist : ", id(mylist))
print("id of mylist[0] : ", id(mylist[0]))
print("id of mylist[1] : ", id(mylist[1]))
print("id of mylist[2] : ", id(mylist[2]))

print('-'*35)
newlist = copy.deepcopy(mylist)
print("id of mylist : ", id(newlist))
print("id of mylist[0] : ", id(newlist[0]))
print("id of mylist[1] : ", id(newlist[1]))
print("id of mylist[2] : ", id(newlist[2]))

newlist[2][1] = 'HELLO'
print(mylist)
print(newlist)