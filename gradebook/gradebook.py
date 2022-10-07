from student import Student
from grade import Grade

class Gradebook:
    def __init__(self):
        self.gradebook = {}
    
    def __str__(self):
        s = ""
        for subject in self.gradebook:
            s += f"{subject}:\n"
            
            for student, grade in self.gradebook[subject]:
                s += f"{student}: {grade}\n"
                
            s += "\n"
        
        return s
    
    def insert_grade(self, subject: str, student: Student, grade: Grade):
        if subject not in self.gradebook:
            self.gradebook[subject] = []
        
        self.gradebook[subject].append((student, grade))
    
    def to_dict(self):
        output = {}
        for subject in self.gradebook:
            output[subject] = []
            
            for student, grade in self.gradebook[subject]:
                output[subject].append((student.to_dict(), grade.to_dict()))
        
        return output
    
    @classmethod
    def from_dict(self, data: dict):
        gb = Gradebook()
        
        for subject in data:
            gb.gradebook[subject] = []
            
            for student, grade in data[subject]:
                gb.gradebook[subject].append(Student.from_dict(student), Grade.from_dict(grade))
        
        return gb