# (A -----> B)
# HERE CLASS B IS INHERITED BY CLASS A

print("SINGLE-INHERITANCE :- 1 CHILD_CLASS INHERIT 1 PARENT_CLASS")

class parent:
    def par(self):
        print("I am parent class")

class child(parent):
    def chi(self):
        print("I am child class")

c = child()
c.par()
c.chi()
