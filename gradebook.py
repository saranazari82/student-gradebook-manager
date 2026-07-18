import student
import course
import assessment
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

    def add_assessment(self,course_code,assessment) :
        if course_code in self.courses :
            course = self.courses[course_code]        
            course.add_assessment(assessment)

    def record_grade(self,student_id,course_code,assessment_title,score) :
        if student_id in self.students and course_code in self.courses :
            if student_id not in self.grades :
                self.grades[student_id] = {}
            if course_code not in self.grades[student_id] :
                self.grades[student_id][course_code] = {}
                self.grades[student_id][course_code][assessment_title] = score

    def calculate_average(self,student_id,course_code) :
        if student_id in self.grades and course_code in self.grades[student_id] :
            course = self.courses[course_code]
            percentages = []
            for title,score in self.grades[student_id][course_code].items() :
                assessment = course.find_assessment(title)
                percentage = assessment.calculate_percentage(score)
                percentages.append(percentage)
            return sum(percentages) / len(percentages)

    def get_result(self,average) :
        if average >= self.passing_grade :
            return "Passed"
        else :
            return "Failed"

    def show_report(self,student_id) :
        if student_id in self.students :
            student = self.students[student_id]
            print(f"===== Student Report =====")
            print(f"Student ID: {student.get_id}")
            print(f"Name: {student.get_name()}")
            print(f"Email: {student.email}")
            if student_id in self.grades :
                for course_code in self.grades[student_id] :
                    course = self.courses[course_code]
                    print(f"Course: {course_code} - {course.course_name}")
                    for title,score in self.grades[student_id][course_code].items() :
                        assessment = course.find_assessment(title)
                        percentage = assessment.calculate_percentage(score)
                        print(f"{title}: {score} / {assessment.max_score} = {percentage}%")
                    average = self.calculate_average(student_id,course_code)
                    result = self.get_result(average)
                    print(f"Average: {average}%")
                    print(f"Result: {result}")

    def search_student(self,keyword) :
        for student in self.students.values() :
            if keyword == student.get_id or keyword in student.get_name() :
                return student
            return None
    
    def delete_student(self,student_id):
        if student_id in self.students :
            del self.students[student_id]
            for course in self.courses.values() :
                if student_id in course.students :  
                    course.students.remove(student_id)  



