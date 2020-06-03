import sqlite3
import pandas as pd

sql = 'SELECT * FROM Lotto'

conn = sqlite3.connect('demo.db')
df = pd.read_sql_query(sql, con=conn)

print(df)

conn.close()
