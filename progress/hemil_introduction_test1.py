# Find the occurance of character in a string.
# input: abbdfgrfddff
# output: [b] 2
# output: [z] 0

a = input("Please Enter Your FullName : ")
x = 0

for i in a:
    if i >= "0" and i <= "9":
        x = 1

if x == 1:
    print("please print only string")
else:
    b = input("which letter you want to count?? ")
    c = a.count(b)
    print("repeated times : ", c)


# print below pattern
#  *****
#  ****
#  ***
#  **
#  *

n = int(input("Enter no. of rows : "))
for i in range(0, n):
    for j in range(i, n):
        print("*", end=" ")
    print()
