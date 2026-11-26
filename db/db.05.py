import oracledb
import os
from dotenv import load_dotenv



load_dotenv()
ora_conn = os.getenv('ora_conn')
conn = oracledb.connect(ora_conn)
# print(conn.version)

cursor = conn.cursor()

# sql = """select region, sum(loan_jan_amt) from kor_loan_status
# group by region
# order by sum(loan_jan_amt) desc"""

#sql = """select * from stuscore"""
sql = """select * from event"""


cursor.execute(sql)

# 모든 데이터 들고 오기
rows = cursor.fetchall()

for row in rows:
    print(row[0],row[1],row[2])

print('열의 수: ',len(rows))
cursor.close()
conn.close()




# 데이터 하나만 들고오기
# # rows = cursor.fetchone()
