"""Chapter class"""


class Chapter:
    def __init__(self, name:str, subject:str, pages:int, grade:int, difficulty:int):
        self.name = name
        self.grade = grade

        self.subject = subject
        self.pages = pages
        self.difficulty_level = difficulty

    def __str__(self):
        return f"{self.name} [Grade {self.grade}] - {self.pages} pages"