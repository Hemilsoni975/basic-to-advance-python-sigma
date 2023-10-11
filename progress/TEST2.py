"""
Write a Python program to get the time from user and find milliseconds in Python
"""

from datetime import datetime

def millisecond():
    time = input("Enter your time (HH:MM:SS): ")

    try:
        user = datetime.strptime(time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please use H:M:S format.")

    else:
        milliseconds = (user.hour * 3600 + user.minute * 60 + user.second) * 1000

        print("Milliseconds: ", milliseconds)

millisecond()
"""
number is prime in a given list of numbers. Return True if all numbers are prime otherwise False. [HEMIL]
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False
"""

user = int(input("how many element you want to add : "))
myList = []

for i in range(0, user):
    ele = int(input("Enter input : "))
    myList.append(ele)

k = 0
for i in myList:
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c = 1


    if c == 0:
        k = k + 1

if k == len(myList):
    print("True")
else:
    print("False")
