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

def get_subjects(grade:int, backend:bool=True):
    db, c = subj_setup(grade)

    c.execute(f"SELECT * FROM subj_{grade}")
    
    subjects = c.fetchall()
    db.close()

    return [(subject[0], eval(subject[1])) for subject in subjects] if backend else subjects

def register_user(self, name:str, grade:int, weak:tuple, strong:tuple, breaks:tuple, holidays:int, hours:int):
    db = sqlite3.connect("./data/users.db")
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, grade TEXT, weak TEXT, strong TEXT, breaks INTEGER, b_duration INTEGER, holiday INTEGER, hours INTEGER)")
    db.commit()

    c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (name, grade, str(weak), str(strong), breaks[0], breaks[1], holidays, hours))
    db.commit()

    db.close()


    
