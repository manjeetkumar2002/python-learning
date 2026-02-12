#Ques : To create details of 5 students in a list ,getting the input using the keyboard
        # Find the highest marks of student and calculate the average.
        # display the grade of the student based on the average
        # delete the whose average marks are below 40



def InputStudentsData():
    print("Enter Students Data : \n ")
    studentsList = []
    for i in range(5):
        student = dict()
        name = input("Enter student name: ")
        course = input("Enter course: ")
        marks = int(input("Enter marks: "))

        student["Name"] = name
        student["Course"] = course
        student["Marks"] = marks

        studentsList.append(student)

    return studentsList

def calculateHighestMarks(studentList):
    maximum = 0

    for student in studentList:
        if student["Marks"] > maximum:
            maximum = student["Marks"]

    return maximum

def calculateAverageMarks(studentList):
    average = 0

    for student in studentList:
        average += student["Marks"]

    return average / len(studentList)


students = InputStudentsData()

def printStudents(studentList):
    print("[")
    for student in students:
        print(student)
    print("]")

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

print("\nDetails of students are : \n")
printStudents(students)

print("\nThe highest marks are : ")
highestMarks = calculateHighestMarks(students)
print(highestMarks)

print("The average marks of students are : ")
averageMarks = calculateAverageMarks(students)
print(averageMarks)


print(f"Deleting the student whose marks is below the average 40 :")

for student in students:
    if student["Marks"] < 40:
        students.remove(student)

print("Student details after deleting is : ")
printStudents(students)


print("Grade of all students based on marks : ")

for student in students:
    grade = get_grade(student["Marks"])
    student["Grade"] = grade

printStudents(students)
