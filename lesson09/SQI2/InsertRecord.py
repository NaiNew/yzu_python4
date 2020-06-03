import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'Taipei', 20000.00 )")

cursor.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Taipei', 15000.00 )")

cursor.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Taoyuan', 20000.00 )")

cursor.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'New-Taipei ', 65000.00 )")

conn.commit()
print("Records created successfully")
conn.close()
