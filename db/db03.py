import oracledb
import os
from dotenv import load_dotenv



load_dotenv()
ora_conn = os.getenv('ora_conn')
conn = oracledb.connect(ora_conn)
# print(conn.version)

cursor = conn.cursor()
no = 3
name = '이순신'
school = '신림고'
rank = 3
height = 190
kor = 80
eng = 90 
math = 60
total = kor+eng+math
avg = round(total/3,2)
specialty = 'python'
scorerank = 0

# sql = f'insert into stuscore2 values({no},{name},{school},{rank},{height},{kor},{eng},{math},{total},{avg},{specialty},{scorerank})'
# cursor.execute(sql)
# conn.commit()
# print('저장완료')

# sql = 'insert into stuscore2 values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)'
# cursor.execute(sql, [no, name, school, rank, height, kor, eng, math, total, avg, specialty, scorerank])


sql = "update stuscore2 set height = 160, specialty = 'python' where no = 2"
cursor.execute(sql)

conn.commit()
print('저장완료')

cursor.close()
conn.close()


# 데이터 하나만 들고오기
# # rows = cursor.fetchone()
