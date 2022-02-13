# Write a python script to define a class student having members roll no, name, age, gender. Create a subclass called Test with member marks of 3 subjects. Create three objects of the Test class and display all the details of the student with total marks.


class StudentInfo:
    def getData(self, rollno, name, course, age):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.age = age

    def displayStudent(self):
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Age:", self.age)


class Test(StudentInfo):
    def getMarks(self, marks):
        self.marks = marks

    def displayMarks(self):
        print("Total Marks:", self.marks)

    # Multiple Inheritance


class Result(Test):
    def calculateGrade(self):
        m = self.marks
        if m > 480:
            self.grade = "Distinction"
        elif m > 360:
            self.grade = "FirstClass"
        elif m > 240:
            self.grade = "SecondClass"
        else:
            self.grade = "Failed"
        print("Result:", self.grade)


# Main Program
r = int(input("Enter Roll Number:"))
n = input("Enter Name:")
c = input("Enter Course Name:")
d = input("Enter Age:")
m = int(input("Enter Marks:"))
stud1 = Result()
stud1.getData(r, n, c, d)
stud1.getMarks(m)
stud1.displayStudent()
stud1.displayMarks()
stud1.calculateGrade()
