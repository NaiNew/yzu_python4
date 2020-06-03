import sqlite3

sql = '''
        CREATE TABLE Employee(
            ID INT PRIMARY KEY         NOT NULL,
            NAME           VARCHAR(20) NOT NULL,
            AGE            INT         NOT NULL,
            ADDRESS        VARCHAR(50),
            SALARY         REAL
        );
      '''

conn = sqlite3.connect('company.db')
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
conn.close()
print('Employee 資料表建立完成')
