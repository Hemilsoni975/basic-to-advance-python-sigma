# List is mutable that is it can be update
myList = [1, 2, 3, 4, 5, "hemil", "umang", "tirth", "kshitij", "hetvi"]

print("-----+++++++++-----")

print(myList[0])  # to get specific item from list
print(myList[1])

print("-----+++++++++-----")

print(myList[-4])  # to print negative index in list
print(myList[len(myList)-4])  # to print negative index in list
print(myList[5-4])  # to print positive index in list

print("-----+++++++++-----")

# to print list using for_loop
for lists in myList:
    print(lists)

print("-----+++++++++-----")

# to check whether item is there in list or not
if "hemil" in myList:
    print("wow!!!")
else:
    print("sorry!!!")

print("-----+++++++++-----")

# to print whole list
print(myList[:])
print(myList[1:8])  # slicing in list
print(myList[1:8:2])  # slicing with jump
print(myList[::2])

print("-----LIST COMPREHENSION-----")

# list comprehension
lst1 = [i*i for i in range(10)]
print(lst1)

lst2 = [i*i for i in range(10) if i % 2 == 0]
print(lst2)

# example
wow = ["red", "yellow", "blue" , "green"]
lst3 = [i for i in wow if (len(i) <= 4)]
print(lst3)

print("-----METHODS OF LIST-----")

wow1 = [2, 4, 3, 5, 9, 0]
wow2 = [10, 20, 30, 40, 50]
ok = wow1.copy()  # used for copying one list into another
print(wow1)
print(ok[3])
wow1.sort()  # ascending order
wow1.reverse()  # descending order
print(wow1)
print(max(wow1))  # maximum value of list
print(min(wow1))  # minimum value of list
wow1.append(6)  # insert element in last
print(wow1)
wow1.insert(2, 65)  # insert element at specific index position
print(wow1)
wow1.remove(6)  # it removes specific number
print(wow1)
wow1.pop()  # removes last element from list
print(wow1)
wow1.extend(wow2)  # it helps to extend values of one list into another
print(wow1)
ok = wow1+wow2  # helps in concating two strings
print(ok)
wow1.clear()  # it delete whole list
print(wow1)
