# ABSTRACTION MEANS HIDING THE DATA OR PROCESS BEHIND THE OPERATIONS.
# FOR EXAMPLE :-
# -->   A REAL LIFE EXAMPLE IF ANYONE WANT TO LEARN ABOUT PYTHON THEN HE WILL SEARCH ON
#       THE YOUTUBE ANE HE WILL GET APPROPRIATE RESULT. BY CLICKING ON ANY OF THE VIDEO HE WILL START LEARNING
#       ABOUT PYTHON BUT HE IS UNAWARE ABOUT THE BACK PROCESS LIKE HOW HE GETS THE VIDEO ON SEARCHING.
# -->   ANOTHER BEST EXAMPLE RELATED TO PYTHON IS "PRINT" FUNCTION WHICH HELP US TO PRINT MESSAGE BUT ACTUALLY
#       WE DON'T KNOW THE BACK PROCESS OF THAT PARTICULAR FUNCTION.
# -->   ANOTHER BEST EXAMPLE IS WE CAN TYPE WITH HELP OF KEYBOARD BY PRESSING BUTTONS BUT WE DON'T KNOW THE
#       INTERNAL PROCESS
# IN SHORT, ABSTRACTION MEANS FUNCTIONALITIES ARE KNOW BY USER BUT PROCESS BEHIND THAT FUNCTIONALITTIES ARE NOT
# KNOWN TO US.
# ABSTRACTION IS ALSO A GENERALIZATION LIKE TO HIDE COMPLEC LOGICS.
# ABSTRACTION IS ACHIEVED THROUGH :
# 1) ABSTRACT CLASS  - it contains at least one abstract method compulsory for becoming abstract class
# 2) ABSTRACT METHOD - it is declare inside the class using decorator "@abstractmethod"
# 3) INTERFACE - class that contains all the abstract methods

#  for import abstractmethod from abc module :-

from abc import ABC, abstractmethod

class hello(ABC):
    def hi(self):
        print("I am simple method")

    @abstractmethod
    def hii(self):
        print("I am simple abstract method")
        pass

class wow(hello):

    def hii(self):
        print("hey hello hii")

w = wow()
w.hii()


