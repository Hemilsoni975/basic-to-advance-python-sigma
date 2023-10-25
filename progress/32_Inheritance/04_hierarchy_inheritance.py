# (MAIN_NODES ---> ROOT_NODES----> SUB_NODES)
# HERE SUB_NODES IS INHERITED BY ROOT_NODES WHICH ARE FURTHER INHERITED BY MAIN_NODES.
# HERE SUB_NODES CAN ACCESS ALL THE FUNCTIONS AND METHODS OF ROOT_NODES AND MAIN_NODES ALSO.

print("HIERARCHICAL-INHERITANCE :- ONE ROOT NODE EXTENDES ONE OR MORE PARENT NODES FROM THAT EXTENDES MANY CHILD NODES")

class root:
    def root_node(self):
        print("I am the main base of this inheritance")

class father(root):
    def fparent(self):
        print("I am the father_class inherit the root class")

class mother(root):
    def mparent(self):
        print("I am the mother_class inherit the root class")

class son(father):
    def son1(self):
        print("I am inherited by father_class")

class daughter(mother):
    def dau(self):
        print("I am inherited by mother_class")


s = son()
s.root_node()
s.fparent()
s.son1()
d = daughter()
d.root_node()
d.mparent()
d.dau()
