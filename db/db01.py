import oracledb
import os
from dotenv import load_dotenv



load_dotenv()
ora_conn = os.getenv('ora_conn')
conn = oracledb.connect(ora_conn)
# print(conn.version)

cursor = conn.cursor()

# sql = 'select * from student'
sql = """select school, grade, max(kor+eng+math) from student
group by school, grade
order by school, grade"""

cursor.execute(sql)

# 모든 데이터 들고 오기
rows = cursor.fetchall()

for row in rows:
    print(row)
cursor.close()

# 데이터 하나만 들고오기
# rows = cursor.fetchone()


