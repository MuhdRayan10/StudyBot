"""
Chapter class

difficulty -> time in hours how long it will take to complete the chapter
"""
from math import ceil

class Chapter:
    def __init__(self, name:str, subject:str, pages:int, grade:int, difficulty:int):
        self.name = name
        self.grade = grade

        self.subject = subject
        self.pages = pages
        self.difficulty = difficulty

    def __str__(self):
        return f"{self.name} [Grade {self.grade}] - {self.pages} pages"
    
    def get_time(self, pages:int): # shows time it will take to do x pages of the chapter for the average person, output in minutes
        if pages > self.pages:
            return -1
        
        return ceil((pages / self.pages) * self.difficulty * 60)
    

light = Chapter("Light", "Physics", 27, 10, 3)
print(light.get_time(1))
