class Chapter:
    def __init__(self, chapter_name, pages, difficulty_level):
        self.chapter_name = chapter_name

        self.t_pages = pages
        self.difficulty_level = difficulty_level

    def __str__(self):
        return f"{self.chapter_name} - {self.t_pages} pages"