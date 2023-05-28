from classes.chapter import Chapter

class Subject:
    def __init__(self, name:str, grade:str):
        self.name = name
        self.grade = grade

        # chapters
        self.chapters = []

    def add_chapter(self, chapter:Chapter) -> None:
        self.chapters.append(chapter)
    
    def get_chapter(self, name:str) -> Chapter:
        return [chapter for chapter in self.chapters if Chapter.name == name][0]

    def __repr__(self):
        return f"{self.subject_name} -> Grade ({self.grade})"