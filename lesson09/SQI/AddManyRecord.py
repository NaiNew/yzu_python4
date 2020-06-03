import sqlite3
import random

sql = 'Insert into Lotto(n1, n2, n3, n4 ,n5 ,n6)' \
      'Values (?, ?, ?, ?, ?, ?)'

lottos = []
for i in range(100):
      nums = set()
      while len(nums) < 6:
            nums.add(random.randint(1, 46))
      lottos.append(tuple(nums))

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.executemany(sql, lottos)
id = cursor.lastrowid
print('新增資料成功')
conn.commit()
conn.close()
