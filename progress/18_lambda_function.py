# lambda is one line functions and it is also known as anonymous function
# if user want minimization in code than he can use lambda function directly to call
# lambda function is used in situation where small functions required for short period of time

# print("--------------calulator--------------")
#
# x = int(input("Enter no. : "))
# y = int(input("Enter no. : "))
#
# addition = lambda m, n: m + n
# subtraction = lambda m, n: m - n
# multiplication = lambda m, n: m * n
# division = lambda m, n: m / n
#
# print("FOR ADDITION PRESS 1 ")
# print("FOR SUBTRACTION PRESS 2 ")
# print("FOR MULTIPLICATION PRESS 3 ")
# print("FOR DIVISION PRESS 4 ")
# print("FOR EXIT PRESS 5 ")
#
# while True:
#     a = int(input("Enter your choice : "))
#     if a == 1:
#         print("addition : ", addition(x, y))
#     elif a == 2:
#         print("subtraction : ", subtraction(x, y))
#     elif a == 3:
#         print("multiplication : ", multiplication(x, y))
#     elif a == 4:
#         print("division : ", division(x, y))
#     elif a == 5:
#         print("thanks for visiting!!!")
#         exit()
#     else:
#         print("Invalid choice!!!")


# print("--------sorting_list---------")
# n = []
# for i in range(1, 10):
#     a = input("Enter no: ")
#     n.append(a)
#
# print("before sorting : ", n)
# n.sort(key=lambda x: x)
# print("ascending order : ", n)
# n.reverse()
# print("descending order : ", n)

# you can use small function in form of lambda in high-order functions
def out(fx,value):
    return 10 + fx(value)
print("lambda : ",out(lambda x: x * x, 2))
