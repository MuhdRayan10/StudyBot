from datetime import date


class Exam:
    def __init__(self, name:str, marks:int, chapters:list, grade:int, d:tuple):
        self.exam = name
        self.marks = marks
        self.grade = grade

        self.chapters = chapters
        self.date = d

    def get_time_left(self):
        exam = date(*self.date)
        today = date.today()

        time_left = exam - today
        print(time_left)

        return time_left.days
    

half_yearly = Exam("Half Yearly", 80, ['Light', 'Chemical Reactions'], 10, (2023, 5, 30))
print(half_yearly.get_time_left())

