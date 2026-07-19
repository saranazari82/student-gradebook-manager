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
    if choice == "0" :
        print("Goodbye!")
        exit = True

    elif choice == "1" :
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ").title()
        email = input("Enter Email: ")
        new_student = Student(student_id,name,email)
        gradebook.add_student(new_student)
        print("Student added successfully!")
       
    elif choice == "2" :
        for student in gradebook.students.values() :
            student.display_info()

    elif choice == "3" :
        course_code = input("Enter Course Code : ")
        course_name = input("Enter Course Name: ")
        new_course = Course(course_code,course_name)
        gradebook.add_course(new_course)
        print("Course added successfully!")

    elif choice == "4" :
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code : ")
        gradebook.enroll_student(student_id,course_code)
        print("Student enrolled successfully!")

    elif choice == "5" :
        course_code = input("Enter Course Code : ")
        assessment_type = input("Enter Assessment Type (Quiz/Exam/Project): ").lower()
        title = input("Enter Assessment Title: ")
        max_score = int(input("Enter Max Score: "))
        if assessment_type == "quiz" :
            new_assessment = Quiz(title,max_score)
        elif assessment_type == "exam" :
            new_assessment = Exam(title,max_score)
        elif assessment_type == "project" :
            new_assessment = Project(title,max_score)
        gradebook.add_assessment(course_code,new_assessment)
        print("Assessment added successfully!")

    elif choice == "6" :
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code : ")
        title = input("Enter Assessment Title: ")
        score = int(input("Enter Score: "))
        gradebook.record_grade(student_id,course_code,title,score)
        print("Grade recorded successfully!")
        
    elif choice == "7" :
        student_id = input("Enter Student ID: ")
        gradebook.show_report(student_id)

    
