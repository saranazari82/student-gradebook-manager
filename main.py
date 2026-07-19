from student import Student
from course import Course
from assessment import Quiz,Exam,Project
from gradebook import Gradebook

gradebook = Gradebook(55)
def show_menu():
    print("\n===== Student Gradebook Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. Enroll Student in Course")
    print("5. Add Assignment")
    print("6. Record Grade")
    print("7. View Student Report")
    print("0. Exit")

exit = False
while not exit :
    show_menu()
    choice = input("Choose an option: ") 
    if choice == "1" :
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        new_student = Student(student_id,name,email)
        gradebook.add_student(new_student)
        print("Student added successfully!")
    elif choice == "0" :
        print("Goodbye!")
        exit = True
    elif choice == "2" :
        for student in gradebook.students.values() :
            student.display_info()
    elif choice == "3" :
        course_code = input("Enter Course Code : ")
        course_name = input("Enter Course Name: ")
        new_course = Course(course_code,course_name)
        gradebook.add_course(new_course)
        print("Course added successfully!")

