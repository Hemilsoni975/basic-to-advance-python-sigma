# ( A & B ----> C )
# HERE C CLASS INHERITS CLASS A AND B BOTH.
# IF ANY FUNCTION OR METHOD REMAINS SAME IN BOTH A AND B THEN FUNCTIONS OF CLASS A WILL BE DISPLAYED

print("MULTIPLE-INHERITANCE :- 1 CHILD INHERIT 2 PARENT_CLASS")

class father:
    def parent(self):
        print("I am the father_class")

class mother:
    def parent(self):
        print("I am the mother_class")

    def mparent(self):
        print("I am the mother_class")
class child(father,mother):
    def chi(self):
        print("I am the child_class")

c = child()
c.parent()
c.mparent()
c.chi()
