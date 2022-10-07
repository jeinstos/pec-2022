import json
import random

from gradebook import Gradebook
from student import Student
from grade import Grade

if __name__ == "__main__":
    students = [
        ("Alpha", "Alpha"),
        ("Bravo", "Bravo"),
        ("Charlie", "Charlie"),
        ("Delta", "Delta"),
    ]
    
    grades = [
        0.65,
        0.75,
        0.87,
        0.93,
    ]
    
    subjects = [
        "Chemestry",
        "Physics",
        "Math",
        "English",
        "Writing",
    ]
    
    gb = Gradebook()
    
    for subject in subjects:
        for first_name, last_name in students:
            gb.insert_grade(subject, Student(first_name, last_name), Grade(random.choice(grades)))
    
    with open("gradebook.json", "w") as f:
        json.dump(gb.to_dict(), f, sort_keys=True, indent=4)