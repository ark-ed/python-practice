#init

import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

#cur.execute("CREATE TABLE worker(name,hours_worked,salary)")

cur.execute("""
    INSERT INTO worker VALUES
        ('Michael', 8, 12),
        ('Jake', 9, 14),
        ('Tod', 7, 12)
""")

con.commit()