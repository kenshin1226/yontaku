import sqlite3
conn = sqlite3.connect('yontakudatabase.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM users where seibetu='男' and age<18")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()