import sqlite3

def convert_chapters(chapters:list):
    return [chapter.data_list() for chapter in chapters]

def subj_setup(grade:int):
    db = sqlite3.connect("./data/subjects")
    c = db.cursor()

    c.execute(f"CREATE TABLE IF NOT EXISTS subj_{grade} (name TEXT, chapters TEXT)")
    db.commit()

    return db, c


def add_subect(grade:int, subjects:list):
    db, c = subj_setup(grade)

    for subject in subjects:
        c.execute(f"INSERT INTO subj_{grade} VALUES (?, ?)", (subject.name, str(convert_chapters(subject.chapters))))

    db.commit()
    db.close()

def add_chapter(grade:int, subject:str, chapters:list):
    db, c = subj_setup(grade)

    c.execute(f"SELECT chapter FROM subj_{grade} WHERE name='{subject}'")
    data = c.fetchall()

    if not data: return

    ch = eval(data[0][1])
    ch.extend(convert_chapters(chapters))

    c.execute(f"UPDATE subj_{grade} SET chapters=:c WHERE name=:n", {"c":str(ch), "n":subject})
    db.commit()

    db.close()






