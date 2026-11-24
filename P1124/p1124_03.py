import os
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent.parent
envFile = BASE_DIR / '.env'

# .env 파일 불러오기
load_dotenv(envFile)
api_key = os.getenv('open_ai_key')

# API 키 존재 여부 확인
if not api_key:
    raise RuntimeError('API 키를 불러오지 못했습니다.')

# 여행지 입력
while True:
    txt_input = input('가고 싶은 여행지 입력 >>').strip()
    if txt_input: break
    print('여행지 입력해야 검색 가능')
print('입력 완료')


client = OpenAI(api_key=api_key)

try:
    print('API 연결을 시작합니다.')

    response = client.responses.create(
        model='gpt-5.6',
        instructions="""
        당신은 여행 설계 전문가입니다.
        1박 2일 여행 일정을 설계해주세요.
        여행자는 기차와 대중교통을 이용합니다.
        누구나 이해하기 쉽도록 쉽고 간결하게 답변해주세요.
        """,
        input=f'{txt_input}에 대해 [1박 2일] 여행지, 숙소, 식사 등을 제안해주세요',
        max_output_tokens=1000,
    )

    # API 응답 텍스트 추출
    result = response.output_text.strip()

    if not result:
        raise RuntimeError('api 응답에 표시할 텍스트 없음')

    print('-' * 40)
    print(result)

except openai.APIConnectionError as error:
    print(f'api 연결에러 확인 요망: {error}')

except openai.RateLimitError as error:
    print(f'api 요청한도 확인 요망: {error}')

except openai.APIError as error:
    print(f'api 요청 실패: {error}')




# 결과값
# 가고 싶은 여행지 입력 >>경주
# 입력 완료
# API 연결을 시작합니다.
# ----------------------------------------
# ## 경주 1박 2일 추천 일정  
# **기준:** KTX 경주역 도착·출발 / 버스와 도보 이용

# ### 1일차: 경주 도심 역사 여행

# | 시간 | 일정 |
# |---|---|
# | 10:00 | **경주역 도착** → 시내버스로 황리단길 이동 |
# | 11:00 | 숙소에 짐 보관 |
# | 11:30 | **황리단길 점심** – 경주식 쌈밥 또는 한우 물회 |
# | 13:00 | **대릉원·천마총** 관람 |
# | 14:30 | 황리단길 산책 및 카페 |
# | 16:00 | **첨성대 → 계림 → 교촌마을** 도보 여행 |
# | 18:00 | 저녁 – 한정식, 떡갈비 또는 순두부 |
# | 19:30 | **동궁과 월지 야경** 감상 |
# | 21:00 | 숙소 이동 및 휴식 |

# **추천 간식:** 황남빵, 찰보리빵, 교리김밥

# ---

# ### 2일차: 불국사와 박물관

# | 시간 | 일정 |
# |---|---|
# | 08:00 | 아침 식사 및 체크아웃, 숙소에 짐 보관 |
# | 09:00 | 시내버스로 **불국사** 이동 |
# | 10:00 | 불국사 관람 |
# | 12:00 | 불국사 주변 점심 – 산채비빔밥 또는 순두부 정식 |
# | 13:30 | 버스로 시내 이동 |
# | 14:30 | **국립경주박물관** 관람 |
# | 16:00 | 숙소에서 짐 찾기 |
# | 16:30 | 시내버스로 경주역 이동 |
# | 17:30 이후 | KTX 탑승 |

# ※ **석굴암을 꼭 보고 싶다면** 국립경주박물관 대신 방문하세요. 