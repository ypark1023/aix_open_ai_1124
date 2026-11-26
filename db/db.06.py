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

sql = """select * from stuscore"""
# sql = """select * from event"""
# sql = """
# select emp_name, salary, srank
# from employees, sal_rank
# where salary between low_salary and high_salary
# order by salary desc
# """

# sql = """
# select a.emp_name, a.department_id, b.department_id, b.department_name, a.hire_date
# from employees a, departments b
# where a.department_id = b.department_id and a.department_id >=50
# order by a.department_id
# """

cursor.execute(sql)

# 컬럼만 가져오기 >> 변수 설정 시 필요
columns = [col[0] for col in cursor.description]    #['EMP_NAME', 'SALARY', 'SRANK']
print(columns)

# 모든 데이터 들고 오기
rows = cursor.fetchall()

# for row in rows:
#     print(row)
#     # print(f'직원명: {row[0]}\t연봉: {row[1]}\t등급: {row[2]}')

# row를 딕셔너리로
rows = [dict(zip(columns, row)) for row in rows]
print(rows)


print('열의 수: ',len(rows))
cursor.close()
conn.close()




# 데이터 하나만 들고오기
# # rows = cursor.fetchone()
