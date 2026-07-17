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