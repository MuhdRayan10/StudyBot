class Exam:
    def __init__(self, name:str, marks:int, chapters:list, grade:int, date:tuple):
        self.exam = name
        self.marks = marks
        self.grade = grade

        self.chapters = chapters
        self.date = date

    def get_time_left(self):
        pass

    