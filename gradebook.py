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
            return True
        else :
            return False

    def add_assessment(self,course_code,assessment) :
        if course_code in self.courses :
            course = self.courses[course_code]        
            course.add_assessment(assessment)
            return True
        else :
            return False

    def record_grade(self,student_id,course_code,assessment_title,score) :
        if student_id not in self.students or course_code not in self.courses :
            print("Student or Course not found.")
            return
        course = self.courses[course_code]
        assessment = course.find_assessment(assessment_title)
        if assessment is None :
            print("Assessment not found.")
            return
        if score < 0 or score > assessment.max_score :
            print(f"Invalid score! Must be between 0 and {assessment.max_score}.")
            return
        if student_id not in self.grades :
            self.grades[student_id] = {}
        if course_code not in self.grades[student_id] :
            self.grades[student_id][course_code] = {}
        self.grades[student_id][course_code][assessment_title] = score
        return True

    def calculate_average(self,student_id,course_code) :
        if student_id in self.grades and course_code in self.grades[student_id] :
            course = self.courses[course_code]
            percentages = []
            for title,score in self.grades[student_id][course_code].items() :
                assessment = course.find_assessment(title)
                if assessment :
                    percentage = assessment.calculate_percentage(score)
                    percentages.append(percentage)
            if percentages :        
                return sum(percentages) / len(percentages)
            else :
                return 0

    def get_result(self,average) :
        if average >= self.passing_grade :
            return "Passed"
        else :
            return "Failed"
    
    def get_letter_grade(self,average) :
        if average >= 90 :
            return "A"
        elif average >= 80 :
            return "B"
        elif average >= 70 :
            return "C"
        elif average >= 60 :
            return "D"
        else :
            return "F"  

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
                        if assessment :
                            percentage = assessment.calculate_percentage(score)
                            print(f"{title}: {score} / {assessment.max_score} = {percentage}%")
                    average = self.calculate_average(student_id,course_code)
                    result = self.get_result(average)
                    letter_grade = self.get_letter_grade(average)
                    print(f"Average: {average}%")
                    print(f"Result: {result}")
                    print(f"Letter Grade: {letter_grade}")
        else :
            print("Student not found")            

    def show_dashboard(self) :
        print("=====Dashboard=====")
        print(f"Total Students: {len(self.students)}")
        print(f"Total Courses: {len(self.courses)}")

    def search_student(self, keyword):
        keyword = keyword.lower()
        for student in self.students.values():
            student_id = student.get_id.lower()
            student_name = student.get_name().lower()
            if keyword == student_id or keyword in student_name :
                return student
        return None
    
    def delete_student(self,student_id):
        if student_id in self.students :
            del self.students[student_id]
            for course in self.courses.values() :
                if student_id in course.students :  
                    course.students.remove(student_id) 

    
