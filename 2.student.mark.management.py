class Student:
    # Constructor
    def __init__(self,name_student,id_student,dob):
        self.__name_student = name_student
        self.__id_student = id_student 
        self.__dob = dob

    # Setter and getter of name_student
    def get_name_student(self):
        return self.__name_student
    
    def set_name_student(self,name_student):
        if isinstance(name_student, str) and len(name_student) > 0:
            self.__name_student = name_student
        else: 
            print("Invalid name")

    # Setter and getter of id_student
    def get_id_student(self):
        return self.__id_student
    def set_id_student(self,id_student):
        if isinstance(id_student, str) and len(id_student) > 0:
            self.__id_student = id_student
        else: 
            print("Invalid ID")

    # Setter and getter of dob
    def get_dob(self):
        return self.__dob 
    def set_dob(self,dob):
        if isinstance(dob, str) and len(dob) > 0:
            self.__dob = dob
        else: 
            print("Invalid dob")

    def __str__(self):
        return f"Name: {self.__name_student} ID: {self.__id_student} DoB: {self.__dob}"
  

class Course:
    # Constructor
    def __init__(self,id_course,name_course):
        self.__id_course = id_course
        self.__name_course = name_course
    
    # Setter and getter of id_course
    def get_id_course(self):
        return self.__id_course
    
    def set_id_course(self, id_course):
        if isinstance(id_course, str) and len(id_course) > 0:
            self.__id_course = id_course
        else: 
            print("Invalid ID")

    # Setter and getter of name_course
    def get_name_course(self):
        return self.__name_course
    
    def set_name_course(self, name_course):
        if isinstance(name_course, str) and len(name_course) > 0:
            self.__name_course = name_course
        else: 
            print("Invalid name")

    def __str__(self):
        return f"Name: {self.__name_course} ID: {self.__id_course}"
class Marks:
    # Constructor
    def __init__(self):
        self.__marks = {} # key is tuple (id_student,id_course)

    # Setter and getter of marks
    def set_marks(self,student,course,mark): # student is object of Student, course is object of Course, mark is object of Mark
        if isinstance(mark,(float,int)) and 0 <= mark <= 10:
            self.__marks[student.get_id_student(),course.get_id_course()] = mark # student.get_id_student() call method of object student
        else:
            print("Invalid mark")

    def get_marks(self, student, course):
        key = (student.get_id_student(),course.get_id_course())
        if key in self.__marks:
            return self.__marks[key]
        else:
            print("Mark not found!")
            return None

# Function to input number of courses
def input_num_course():
    return int(input("Input number of courses: "))

#Function to input course information
def input_course_information(courses):
    num_course = input_num_course()
    for _ in range(num_course):
        id_course = input("Enter course ID ")
        name_course = input("Enter course name: ")
        course = Course(id_course, name_course)
        courses.append(course)
    return courses

# Function to check number of courses
def check_course(num_course):
    if (num_course <= 0):
        return False
    else: 
        return True

# Function to input number of students 
def input_num_student():
    return int(input("Input number of students: "))    

# Function to input student information
def input_student_information(students): 
    num_students = input_num_student()
    for _ in range(num_students):
        id_student = input("Enter student ID: ")
        name_student = input("Enter student name: ")
        dob = input("Enter student dob: ")
        student = Student(name_student, id_student , dob)   
        students.append(student)
    return students

# Function to check number of students
def check_student(num_students):
    if (num_students <= 0):
        return False
    else:
        return True
    
# Function in input mark
def input_mark(students, courses, marks): 
    if not check_student(len(students)) or not check_course(len(courses)): 
        print("Please input students and courses first") 
        return 
    for student in students: 
        for course in courses: 
            while True: 
                mark = float(input(f"Enter mark for student {student.get_name_student()} in course {course.get_name_course()}: ")) 
                try: 
                    mark = float(mark) 
                    marks.set_marks(student, course, mark) 
                    break 
                except ValueError: print("Invalid input, please enter a numerical value! ")
    
#Function to print the student, course information
def display_student(students):
    if not students:
        print("No student yet")
    else:
        for student in students:
            print(student)
            
def display_course(courses):
    if not courses:
        print("No course yet")
    else: 
        for course in courses:
            print(course)

# Function to show mark          
def show_mark(marks, students, courses):
    found = False # Biến flag để kiểm tra xem có điểm nào không
    for student in students:
        for course in courses:
            mark = marks.get_marks(student,course)
            if mark is not None:
                found = True
                print(f"Student ID: {student.get_id_student()}, Course ID: {course.get_id_course()} - Mark: {mark}")
    if not found:
        print("No mark yet!")
                    

def menu():
    students = []
    courses = []
    marks = Marks()
    while True:
        print("\n------ Menu ------")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List all students")
        print("5. List all courses")
        print("6. Show marks for a course")
        print("7. Exit")

        choice = int(input("Enter your choice between 1 - 7\n"))
        if (choice == 1):
            students = input_student_information(students)
        elif (choice == 2):
            courses = input_course_information(courses)
        elif (choice == 3):
            input_mark(students, courses, marks)
        elif (choice == 4):
            display_student(students)
        elif (choice == 5):
            display_course(courses)
        elif (choice == 6):
            show_mark(marks, students, courses)
        elif (choice == 7):
            print("-------Existing-------")
            break
        else: 
            print("Invalid choice, try again")

menu()
