from chapter import Chapter

class Subject:
    def __init__(self, name:str, code:str):
        self.name = name
        self.subject_code = code

        # chapters
        self.chapters = []

    def add_chapter(self, chapter:Chapter) -> None:
        self.chapters.append(chapter)
    
    def get_chapter(self, name:str) -> Chapter:
        return [chapter for chapter in self.chapters if Chapter.name == name][0]

    def __repr__(self):
        return f"{self.subject_name}({self.subject_code})"