import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    group_name TEXT NOT NULL
)
""")

# Добавляем студента, только если его ещё нет
cur.execute(
    "SELECT 1 FROM students WHERE last_name=? AND first_name=? AND group_name=?",
    ("Dublyanin", "Miron", "3ип-3-24"),
)
if cur.fetchone() is None:
    cur.execute(
        "INSERT INTO students (last_name, first_name, group_name) VALUES (?, ?, ?)",
        ("Dublyanin", "Miron", "3ип-3-24"),
    )
    conn.commit()

# Вывод всех студентов
for row in cur.execute("SELECT * FROM students"):
    print(row)

conn.close()