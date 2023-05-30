import sqlite3

def add_subect(grade:int, subjects:list):
    db = sqlite3.connect("./data/subjects")
    c = db.cursor()

    c.execute(f"CREATE TABLE IF NOT EXISTS subj_{grade} (name TEXT, chapters TEXT)")
    db.commit()

    for subject in subjects:
        c.execute(f"INSERT INTO subj_{grade} VALUES (?, ?)", (subject.name, str(subject.chapters)))

    db.commit()
    db.close()

def add_chapter(grade:int, subject:str, chapters:list):
    db = sqlite3.connect("./data/subjects")
    c = db.cursor()





