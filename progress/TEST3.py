# Dictionary Comprehension - Word Length [Use File Handling]


def write_mode(sf):
    def mode():
        z = sf()
        with open("test3.txt", "w") as x:
            return x.writelines(["baba black ship\n", "hello\n", "heyyy budddy"])
    return mode

@write_mode
def read_mode():
    with open("test3.txt", "r") as f:
        r = f.read().split()

    for i in r:
        l = {i: len(i)}
        print(l)

read_mode()




# Given two lists, create a list of all possible pairs (as tuples) where the first element is less than the second element.
# [use decorator, Comprehension] [HEMIL]
# Input:
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# Output:
# [(1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6)]

user = int(input("Enter how many elments : "))

l1 = []
for i in range(1, user+1):
    a = int(input(f"enter no{i} : "))
    l1.append(a)

l2 = []
for j in range(1, user+1):
    a = int(input(f"enter no{j} : "))
    l2.append(a)

print(l1)
print(l2)

l = [(x,y) for x in l1 for y in l2 if x != y]
print(l)

