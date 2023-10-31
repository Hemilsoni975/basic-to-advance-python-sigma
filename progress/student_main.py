# class
# object
# abstraction
# constructor
# polymorphism
# encapsulation
# destructor

from test4_student_abstract import wow


class SOU(wow):
    def __init__(self, cn):
        super().__init__()
        self.clg_name = cn
        self.college = []

    def add_college(self, cllg):
        self.college.append(cllg)

    def displayInfo(self):
        print(f"UNIVERSITY NAME : {self.clg_name}")

class College(wow):

    def __init__(self, hod):
        self.hod = hod
        self.branch = []

    def add_branch(self, branches):
        self.branch.append(branches)

    def displayInfo(self):
        print(f"NAME OF DEAN : {self.hod}")

class course(wow):
    def __init__(self, name, sub_code):
        self.name = name
        self.sub_code = sub_code
        self.course = []

    def add_course(self,courses):
        self.course.append(courses)

    def displayInfo(self):
        print(f"SELECTED COURSE : {self.name}\nSUBJECT CODE : {self.sub_code}")

class Student():

    def __init__(self, sname, enroll, college, sem):
        self.sname = sname
        self.enroll = enroll
        self.college = college
        self.sem = sem

    def displayInfo(self):
        print(f"NAME OF STUDENT IS {self.sname} WITH ENROLLMENT NO. {self.enroll} STUDIES IN {self.college}\nHE LIKE {self.sem} language")


class head:
    def __init__(self):
        self.__pName = "XYZ"
        self.__pNum = 9876543210
        self.__pProfession = "TEACHER"
        self.__pSalary = 100000
        self.__pLecture = ["python", "java"]

    def __pDisplay(self):
        print(f"""PRINCIPLE NAME : {self.__pName}\nPRINCIPLE NUMBER : {self.__pNum}\nPRINCIPLE PROFESSION : {self.__pProfession}\nPRINCIPLE SALARY : {self.__pSalary}\nPRINCIPLE LECTURE : {self.__pLecture}""")

    def displayPrivateData(self):
        self.__pDisplay()

    def __del__(self):
        print("THE OBJECT HAS DELETED")


# UNIVERSITY NAME
name = input("ENTER COLLEGE NAME : ")
clg_name = SOU(name)

# HOD

HOD = input("ENTER NAME OF DEAN : ")
a = College(HOD)




# STUDENT DETAIL
sname = input("ENTER NAME OF STUDENT : ")
enroll = int(input("ENTER ENROLLMENT OF STUDENT : "))
college = input("ENTER DEGREE OF STUDENT : ")
sem = input("ENTER SEMESTER : ")
s = Student(sname, enroll, college, sem)

# COURSE DETAIL
name = input("ENTER SUBJECT NAME : ")
sub_code = input("ENTER SUBJECT CODE : ")
c = course(name, sub_code)


# display uni name
clg_name.displayInfo()

# display hod
a.displayInfo()


# display student details
s.displayInfo()

# display course
c.displayInfo()

# private method
h = head()
print(h.displayPrivateData())
del h