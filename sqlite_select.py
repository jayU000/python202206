import sqlite3 as sql

conn = sql.connect("database.db")
cur = conn.cursor()

# 디비 데이터 가져오기
# "SELECT * FROM test WHERE col1 = 100"     
#  select 뒤에 가져올 항목  where 뒤에 조건
query = "SELECT col1, col2, col3 FROM test"
cur.execute(query)
rows = cur.fetchall()

for r in rows:
    print(r)

conn.close()