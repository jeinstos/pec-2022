class Grade:
    def __init__(self, percent: float=0.0):
        self.percent = percent
    
    def __str__(self):
        return f"{self.get_letter_grade()} ({self.get_percent_grade()})"
    
    def get_letter_grade(self):
        if self.percent < 0.60:
            return "F"
        elif self.percent < 0.70:
            return "D"
        elif self.percent < 0.80:
            return "C"
        elif self.percent < 0.90:
            return "B"
        else:
            return "A"
    
    def get_percent_grade(self):
        normalized = round(self.percent * 100.0, 2)
        return f"{normalized}%"
    
    def to_dict(self):
        return { "grade" : self.percent }
    
    @classmethod
    def from_dict(cls, data: dict):
        if "grade" not in data:
            raise Exception("missing grade data")
        
        grade = Grade()
        grade.percent = data["grade"]
        
        return grade

print(Grade(0.73))