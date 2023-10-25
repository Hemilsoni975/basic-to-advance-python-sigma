# INHERITANCE :- CHILD CLASS INHERIT THE PROPERTY OF PARENT CLASS
# REPRESENTS REAL-WORLD RELATIONSHIPS AS WELL
# PROVIDES REUSABILITY OF CODE AS USER CAN DIRECTLY CALL FUNCTIONS BY INHERITING EXISTING CLASS TO NEW CLASS.
# PARENT CLASS IS CLASS THAT IS MAIN BASE ALSO CALLED AS BASED CLASS OR SUPER CLASS
# CHILD CLASS IS CLASS THAT IS INHERITED FROM MAIN BASE ALSO CALLED AS DERIVED CLASS OR SUB CLASS
# TYPES OF INHERITANCE :
# 1) SINGLE-INHERITANCE
# 2) MULTILEVEL-INHERITANCE
# 3) MULTIPLE-INHERITANCE
# 4) HIERARCHICAL-INHERITANCE
# 5) HYBRID-INHERITANCE

print("-----------------------------------INHERITANCE-----------------------------------")
class parent:

    def wow(self):
        print("I AM BASE CLASS")

class child(parent):

    def wow1(self):
        print("I AM DERIVED CLASS")

p = parent()
p.wow()
# p.wow1() # function of child class cannot be called by parent class
c = child()
c.wow()
c.wow1()


print("--------------------------INHERITANCE USING CONSTRUCTOR--------------------------")
class hemil:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class soni(hemil):
    def getInfo(self):
        print(f"NAME : {self.name}\nAGE : {self.age}")

s = soni("hemil", 18)
s.getInfo()
