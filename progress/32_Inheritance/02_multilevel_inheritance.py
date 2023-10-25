#  ( A ----> B -----> C)
#  HERE CLASS C CAN ACCESS PROPERTIES OF CLASS B AND A AS IT INHERITS THE CLASS B WHICH IS
#  FURTHER INHERITED BY CLASS A


print("MULTILEVEL-INHERITANCE :- 1 CHILD INHERIT 1 PARENT THAT IS INHERITED BY 1 MAIN_CLASS")

class grand:
    def main(self):
        print("I am the grandparent")

class parent(grand):
    def base(self):
        print("I am the parent class")

class child(parent):
    def derived(self):
        print("I am the child class")

c = child()
c.main()
c.base()
c.derived()
