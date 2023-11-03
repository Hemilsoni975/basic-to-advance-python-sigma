# # class
# # object
# # abstraction
# # constructor
# # polymorphism
# # encapsulation
# # destructor

from test4_student_abstract import wow

cs = []
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

class course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name


class Student(wow):

    def __init__(self, sname, enroll, college, sem):
        self.sname = sname
        self.enroll = enroll
        self.college = college
        self.sem = sem
        self.courses = []

    def sub(self, course):
        self.courses.append(course)

    def displayCourse(self):
        if not self.courses:
            print("NO SUBJECT SELECTED!!!")
        else:
            print("SUBJECT :")
            for course in self.courses:
                print(f"COURSE CODE : {course.course_code}, COURSE NAME : {course.course_name}")

    def displayInfo(self):
        print(f"{self.sname} WITH {self.enroll} OF {self.college} HAS SELECTED {cs} SUBJECTS")

class head:
    def __init__(self):
        self.__pName = "XYZ"
        self.__pNum = 9876543210
        self.__pProfession = "TEACHER"
        self.__pSalary = 100000
        self.__pLecture = ["PYTHON", "JAVA"]

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


while True:
    print("Select an option:")
    print("1. SELECT SUBJECTS")
    print("2. FINISH")


    choice = input("Enter your choice: ")

    if choice == "1":
        course_code = input("ENTER SUBJECT CODE : ")
        course_name = input("ENTER SUBJECT NAME : ")

        c = course(course_code, course_name)

        print(c.course_code)
        print(c.course_name)


        cs.append(c.course_name)
        print("Course created successfully!")

    elif choice == "2":

        # display universty name
        clg_name.displayInfo()

        # display dean
        a.displayInfo()

        # display student details
        s.displayInfo()

        # private method
        # h = head()
        # print(h.displayPrivateData())
        # del h

        exit()
