# class A:
#     def display(self):
#         print("Display from A")
# class B(A):
#     def display(self):
#         print("Display from B")
# class C:
#     def display(self):
#         print("Display from C")
# class D(B, C):
#     def display(self):
#         print("Display from D")
#
# d1 = D()
# # d1.display()
# print(D.mro())


# example2
class University(object) :
    university_name = "SGT"
    def show_details(self):
        print("university name = ",self.university_name)
class Course(University) :
    course_name = "CSC"
    def show_details(self):
        print("course name = ",self.course_name)
class Branch(University):
    branch_name = "Computer Science"
    def show_details(self):
        print("Branch name = ",self.branch_name)

class Student(Course,Branch):
    def __init__(self,name):
        self.name = name
    def show_details(self):
        University.show_details(self)
        Branch.show_details(self)
        Course.show_details(self)
        print("Student name = ",self.name)

class Faculty(Branch):
    def __init__(self,name):
        self.name = name
    def show_details(self):
        University.show_details(self)
        Branch.show_details(self)
        print("Faculty name = ",self.name)

print("\nStudent Details :-\n")
s1 = Student("Manjeet")
s1.show_details()
print("\nFaculty Details :-\n")
f1=Faculty("Jenny")
f1.show_details()