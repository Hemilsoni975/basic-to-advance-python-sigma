# loops is used to print same statements infinite time
# types of for_loop and while_loop

#FOR_LOOP

# simple for_loop using range function
x = 100
for x in range(1,50,2):
    print(x)

# for loop using list
mylist = ["wow", "how", "what", "why"]
for a in mylist:
    print(a)

nice = [["hemil", 975], ["kesar", 906], ["sanjay", 808], ["smit", 965]]
for list1 in nice:
    print(list1)

nice = [["hemil", 975], ["kesar", 906], ["sanjay", 808], ["smit", 965]]
for list1, roll in nice:
    print(list1, roll)

# print multiplication table using for_loop
num = int(input("Enter number : "))

for i in range(1, 11):
    print(num, "*", i, "=", num*i)

# WHILE_LOOP
# it works till the loop is fully executed

i = 0
while i < 50:
    print(i)
    i = i+1

# print multiplication table using while_loop
num = int(input("Enter number : "))
i = 1
while(i <= 10):
    print(num, "*", i, "=", num*i)
    i = i+1

n = int(input("enter no. of rows : "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()


for i in range(5):
    for j in range(i + 1):
        print(i, end="")
    print()


for i in range(5):
    for j in range(i + 1):
        print(j, end="")
    print()
