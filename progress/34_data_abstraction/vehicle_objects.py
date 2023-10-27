from vehicle_methods import *

print(f"1 for bike\n2 for car\n3 for Auto\n4 for exit")

while True:
    choice = int(input("Enter choice : "))
    if choice == 1:
        x = int(input("enter no. tyre of your bike : "))
        z = input("enter color of your bike: ")
        b = Bike(x, z)
        b.display()
    elif choice == 2:
        x = int(input("enter no. tyre of your car : "))
        y = int(input("enter no. gear of your car: "))
        c = Car(x, y)
        c.display()
    elif choice == 3:
        x = int(input("enter no. tyre of your auto : "))
        a = Auto(x)
        a.display()
    elif choice == 4:
        exit()
    else:
        print("Enter valid choice!!!")