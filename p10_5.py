import sqlite3


connection = sqlite3.connect("p10.sl3", 5)
cur = connection.cursor()
cur.execute("DELETE FROM name='Lili' WHERE rowid=5")
connection.commit()
connection.close()
