# ENCAPSULATION IS IDEA OF  WRAPPING DATA AND METHODS THAT WORK ON DATA WITHIN ONE UNIT.
# CLASS IS THE BEST EXAMPLE OF ENCAPSULATION
# IN ENCAPSULATION THE DATA OF ONE CLASS IS HIDDEN FROM ANOTHER CLASS
# IN PYTHON ENCAPSULATION IS ACHIEVED WITH USE OF ACCESS MODIFIER AND GETTERS AND SETTERS METHODS


print()
print("=====================PUBLIC-PRIVATE-PROTECTED=====================")
print()


class Student:

    def __init__(self, name, roll, age):
        self.name = name  # public instance variable
        self._roll = roll  # protected instance variable
        self.__age = age  # private instance variable

    def __display(self):
        print(f"Name : {self.name} Roll no. : {self._roll} Age : {self.__age}")

    def displayPrivateData(self):
        self.__display()


class Branch(Student):
    def show(self):
        print(f"Roll no. : {self.__roll}")


b = Branch("Hemil", 12, 20)
# b.show()
# b.displayPrivateData()  # public method can direct accessed the private method presented in it
# b._Branch__display()  # here child class also can't access the parent class private method using name mangling it
#                       # will throw an error 'Branch' object has no attribute '_Branch__display'

s = Student("Hemil", 12, 20)
print(s.name)
print(s._roll)
print(s._Student__age)  # using name mangling you can easily access private variable
# print(s.__age)   # this can't be accessed it will throw an error 'Student' object has no attribute '__age'
s._Student__age = 40  # after updating it will print 40 not 20
s._Student__display()  # using name mangling


print()
print("=====================GETTER-AND-SETTER-METHODS=====================")
print()
# GETTER METHOD IS USED TO ACCESSED PRIVATE DATA.
# SETTER METHOD IS USED TO SET OR TO MODIFY THE VALUES.
# GETTER AND SETTER IS USED WHEN WE WANT TO APPLY VALIDATION LOGIC
class Student:

    def __init__(self, name, roll, age):
        self.name = name  # public instance variable
        self._roll = roll  # protected instance variable
        self.__age = age  # private instance variable

    def get_age(self):   # getter method help to directly print age
        return self.__age

    def set_age(self, age):
        if age > 40:
            print("Invalid age given.. Age should less than 40")
        else:
            self.__age = age
    # def __display(self):
    #     print(f"Name : {self.name} Roll no. : {self._roll} Age : {self.__age}")
    #
    # def displayPrivateData(self):
    #     self.__display()


# class Branch(Student):
#     def show(self):
#         print(f"Roll no. : {self.__roll}")

s= Student("hemil",20,25)
print(s.get_age())
s.set_age(45)
print(s.get_age())

