import random
import sqlite3 as sql
import string

conn = sql.connect("database.db")       # 데이터베이스 생성


# query = """CREATE TABLE test (                # 처음에 테이블 생성할 때 사용한 명령문
                            # 아래엔 한 번 만들었으므로 없으면 테이블을 생성하기 위해 'IF NOT EXISTS'을 추가
query = """CREATE TABLE IF NOT EXISTS test (        
    col1 INTEGER PRIMARY KEY AUTOINCREMENT,
    col2 VARCHAR(200) NOT NULL,
    col3 TEXT default "")"""

cur = conn.cursor()
cur.execute(query)
conn.commit()

for i in range(1000):
    # parameterized query  쿼리문에서는 ?로 value를 지정하고 나중에 execute로 값을 넣어줌
    query = "INSERT INTO test (col2, col3) VALUES (?, ?)"       
    rnd = "".join([random.choice(string.ascii_letters+string.digits) for i in range(10)])
    print(rnd)
    cur.execute(query, (i, rnd))
conn.commit()





