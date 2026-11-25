import oracledb
import os
from dotenv import load_dotenv



load_dotenv()
ora_conn = os.getenv('ora_conn')
conn = oracledb.connect(ora_conn)
# print(conn.version)

cursor = conn.cursor()

# sql = 'select * from student'

## 문제1
# while True:
#     kor = int(input('몇 점 이상 학생 검색할까요? >> '))
#     if kor == '' : break

#     #실행문
#     sql = f'select * from student where kor>={kor}'
#     cursor.execute(sql)

#     # 모든 데이터 들고 오기
#     rows = cursor.fetchall()

#     for row in rows:
#         print(row)

#     print('인원수: ',len(row))
# cursor.close()

## 문제2
# while True:
#     avg = int(input('평균 몇 점 이상 학생 검색할까요? >> '))
#     if avg == '' : break

#     #실행문
#     sql = f'select * from student where (kor+eng+math)/3>={avg}'
#     cursor.execute(sql)

#     # 모든 데이터 들고 오기
#     rows = cursor.fetchall()

#     for row in rows:
#         print(row)

#     print('인원수: ',len(rows))
# cursor.close()


# ## 문제3
# sql = f"select * from student where lower(name) like '%b%'"
# cursor.execute(sql)
# rows = cursor.fetchall()
# print(rows)
# print('인원수: ',len(rows))

## 문제4

subject_map = {'국어': 'kor', '영어': 'eng', '수학': 'math'}

while True:
    subject = input('검색 과목명(국어,영어,수학) >> ')

    subject1 = subject_map[subject]  # 예: '국어' -> 'kor'
    
    if subject1 == '' : break

    #실행문
    sql = f"select name, {subject1} from student order by {subject1} desc"
    cursor.execute(sql)

    # 모든 데이터 들고 오기
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    print('인원수: ',len(rows))
cursor.close()



# 데이터 하나만 들고오기
# # rows = cursor.fetchone()
