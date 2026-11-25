import oracledb
import os
from dotenv import load_dotenv

load_dotenv
print(os.getenv('ora_id'))


# # 오라클db 불러오기 접속1
conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/XE')
# 접속2
# conn = oracledb.connect('ora_user/1111@localhost:1521/XE')
# # 접속3
# conn = oracledb.connect(ora_conn)


cursor = conn.cursor()

sql = 'select * from stuscore'
cursor.execute(sql)

rows = cursor.fetchall()
# print(rows)

for row in rows:
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t'.format(*row))