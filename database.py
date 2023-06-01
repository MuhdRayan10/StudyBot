import sqlite3

def convert_list(chapters:list):
    li = [chapter.data_list() for chapter in chapters]


def subj_setup(grade:int):
    db = sqlite3.connect("./data/subjects")
    c = db.cursor()

    c.execute(f"CREATE TABLE IF NOT EXISTS subj_{grade} (name TEXT, chapters TEXT)")


def add_subect(grade:int, subjects:list):
    db = sqlite3.connect("./data/subjects")
    c = db.cursor()

    c.execute(f"CREATE TABLE IF NOT EXISTS subj_{grade} (name TEXT, chapters TEXT)")
    db.commit()

    for subject in subjects:
        c.execute(f"INSERT INTO subj_{grade} VALUES (?, ?)", (subject.name, convert_list(subject.chapters)))

    db.commit()
    db.close()

def add_chapter(grade:int, subject:str, chapters:list):
    db = sqlite3.connect("./data/subjects")
    c = db.cursor()







