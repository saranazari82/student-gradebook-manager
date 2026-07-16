class Student :
    def __init__(self,student_id,name,email) :
        self.__student_id = student_id
        self.name = name
        self.email = email
        self.courses = []

    @property    
    def get_id(self) :
        return self.__student_id
     
    def get_name(self) :
        return self.name
    
    def set_email(self,new_email) :
        if "@" in new_email and "." in new_email  :
            self.email = new_email
        else :
            print("invalid email address.")

    def enroll_course(self,course_code) :
        if course_code not in self.courses :
            self.courses.append(course_code)

    def display_info(self) :
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Enrolled Courses: {self.courses}")
