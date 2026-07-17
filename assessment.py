class Assessment :
    def __init__(self,title,max_score):
        self.title = title
        self.max_score = max_score
    
    def calculate_percentage(self,score) :
        return (score/self.max_score)*100
    
    def grade_message(self,score) :
        percentage = self.calculate_percentage(score)
        if percentage >= 90 :
            return "Excellent!"
        if percentage >= 70 : 
            return "Good"
        if percentage >= 50 :
            return "Acceptable"
        else :
            return "Need for greater effort"
        
    def display_info(self) :
        print(f"Assessment Title: {self.title}")
        print(f"Maximum Score: {self.max_score}")





class Quiz(Assessment) :
    def grade_message(self, score) :
        percentage = self.calculate_percentage(score)
        if percentage >= 90 :
            return "Great quiz result!"
        if percentage >= 70 : 
            return "Good quiz performance"
        if percentage >= 50 :
            return "You passed, but review this topic"
        else :
            return "You need to practice this topic more"

    def display_info(self) :
            print(f"Quiz assessment: {self.title}")
            print(f"Quiz Maximum Score: {self.max_score}")





class Exam(Assessment) :
    def grade_message(self, score) :
        percentage = self.calculate_percentage(score)
        if percentage >= 50 :
            return f"You Passed exam! ({percentage}%)" 
        else :
            return f"You Failed exam! ({percentage}%)" 
        
    def display_info(self):
        print(f"Exam: {self.title}")
        print(f"Exam Maximum Score: {self.max_score}")
     