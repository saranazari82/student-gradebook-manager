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
    print("8. Search Student")
    print("9. Update Student Email ")
    print("10. Delete Student")
    print("11. Dashboard")
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
        success = gradebook.enroll_student(student_id,course_code)
        if success :
            print("Student enrolled successfully!")
        else :
            print("Enrollment failed! Check student id and course code.")

    elif choice == "5" :
        course_code = input("Enter Course Code : ")
        assessment_type = input("Enter Assessment Type (Quiz/Exam/Project): ").lower()
        if assessment_type not in ["quiz","exam","project"] :
            print("Invalid assessment type!")
        else :
            title = input("Enter Assessment Title: ")
            max_score_input = input("Enter Max Score: ")
            if max_score_input.isdigit() :
                max_score = int(max_score_input)
                if assessment_type == "quiz" :
                    new_assessment = Quiz(title,max_score)
                elif assessment_type == "exam" :
                    new_assessment = Exam(title,max_score)
                elif assessment_type == "project" :
                    new_assessment = Project(title,max_score)
                success = gradebook.add_assessment(course_code,new_assessment)
                if success :
                    print("Assessment added successfully!")
                else :
                    print("Failed to add assessment! Course not found.")

    elif choice == "6" :
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code : ")
        title = input("Enter Assessment Title: ")
        score_input = input("Enter Score: ")
        if score_input.isdigit() :
            score = int(score_input) 
            success = gradebook.record_grade(student_id,course_code,title,score)
            if success :
                print("Grade recorded successfully!")
            else :
                print("Failed to record grade!")

    elif choice == "7" :
        student_id = input("Enter Student ID: ")
        gradebook.show_report(student_id)

    elif choice == "8" :
        keyword = input("Enter keyword for search: ")
        result = gradebook.search_student(keyword)
        if result :
            result.display_info()
        else :
            print("Student not found!")

    elif choice == "9" :
        student_id = input("Enter Student ID: ")
        if student_id in gradebook.students :
            new_email = input("Enter New Email: ")
            success = gradebook.students[student_id].set_email(new_email)
            if success :
                print("Email updated successfully!")
        else :
            print("Student not found!")        

    elif choice == "10" :
        student_id = input("Enter Student ID: ") 
        if student_id in gradebook.students :
            gradebook.delete_student(student_id) 
            print("Student deleted successfully!")
        else :
            print("Student not found!")    

    elif choice == "11" :
        gradebook.show_dashboard()

    else :
        print("Invalid option! Please choose a number between 0 and 11.")

    

    
