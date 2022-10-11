# Practice on sqlite3
# Documentation: https://docs.python.org/3/library/sqlite3.html

import sqlite3

con = sqlite3.connect('employees.db')
cur = con.cursor()

#cur.execute("CREATE TABLE worker(name,hours_worked,salary)")

#cur.execute("""
#    INSERT INTO worker VALUES
#        ('Michael', 8, 12),
#        ('Jake', 9, 14),
#        ('Tod', 7, 12)
#""")

#data = [
#    ('Greg', 12, 13),
#    ('Addison', 8, 12),
#    ('Jessica', 9, 13),
#]

#cur.executemany("INSERT INTO worker VALUES (?,?,?)",data)

con.commit()