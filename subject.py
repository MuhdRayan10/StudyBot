import Chapter

class Subject:
    def __init__(self, subject_name, subject_code):
        self.subject_name = subject_name
        self.subject_code = subject_code

        # chapters
        self.chapters = []

    def add_chapter(self, chapter: Chapter) -> None:
        self.chapters.append(chapter)
    
    def get_chapter(self, chapter_name:str) -> Chapter:
        return [chapter for chapter in self.chapters if chapter.chapter_name == chapter_name][0]

    def __str__(self):
        return f"{self.subject_name}({self.subject_code})"

    def __repr__(self):
        return f"{self.subject_name}({self.subject_code})"