class Student:
    def __init__(self, first_name: str="", last_name: str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.suspended = False
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def suspend(self):
        self.suspended = True
    
    def to_dict(self):
        return {
            "firstname" : self.first_name,
            "lastname" : self.last_name,
            "suspended" : self.suspended,
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        if "firstname" not in data or "lastname" not in data:
            raise Exception("missing student data")
        
        student = Student()
        student.first_name = data["firstname"]
        student.last_name = data["lastname"]
        student.suspended = data["suspended"]
        
        return student
