import student
import course
class Gradebook :
    def __init__(self,passing_grade) :
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = passing_grade
    
    def add_student(self,student) :
        self.students[student.get_id] = student 

    def add_course(self,course) :
        self.courses[course.course_code] = course
    
    def enroll_student(self,student_id,course_code) :
        if student_id in self.students and course_code in self.courses :
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course_code)
            course.add_student(student_id)
