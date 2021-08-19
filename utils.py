import sqlite3
import datetime
DATABASE_NAME = "database.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table():
    db = get_db()
    c = db.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS "notice"(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        notice TEXT,
        added_at INTEGER
    )
    """)

def add_notice(notice):
    db = get_db()
    c = db.cursor()
    try:
        c.execute("INSERT INTO notice(notice, added_at) VALUES(?, ?)", [notice, datetime.datetime.now()])
        db.commit()
        db.close()
        return "Success"
    except Exception as e:
        return str(e)


def get_notices():
    db = get_db()
    c = db.cursor()
    try:
        data = c.execute("SELECT * FROM notice")
        notices = data.fetchall()
        resp = []
        for i, notices in enumerate(notices):
            resp.append({
                "id" : notices[0],
                "notice" : notices[1],
                "added_at" : notices[2]
            })
        db.commit()
        db.close()
        return resp
    except Exception as e:
        return str(e)
