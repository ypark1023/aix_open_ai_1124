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
    txt_input = input('관심 주식 분야 입력 >>').strip()
    if txt_input: break
    print('주식 분야 입력해야 검색 가능')
print('입력 완료')


client = OpenAI(api_key=api_key)

try:
    print('API 연결을 시작합니다.')

    response = client.responses.create(
        model='gpt-5.6',
        instructions="""
        당신은 주식 전문가 애널리스트입니다.
        2027년 해당 분야를 전망해주세요.
        누구나 이해하기 쉽도록 쉽고 간결하게 답변해주세요. 500자 이내로.
        """,
        input=f'{txt_input}에 대해 2027년 전망을 분석해주세요',
        max_output_tokens=500,
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


# 관심 주식 분야 입력 >>전기차
# 입력 완료
# API 연결을 시작합니다.
# ----------------------------------------
# **2027년 전기차 전망**

# - 전기차 판매는 보조금 축소에도 배터리 가격 하락과 충전망 확대로 꾸준히 증가할 전망입니다.  
# - 저가형 모델 출시가 늘며 내연기관차와의 가격 차이가 줄어듭니다.  
# - 중국 업체의 가격 경쟁력은 강해지고, 기존 완성차 업체는 수익성 압박을 받을 수 있습니다.  
# - LFP 배터리 확대와 전고체 배터리 상용화 기대가 커집니다.  
# - 다만 경기 둔화, 관세·규제, 충전 인프라 부족은 위험 요인입니다.

# **투자 관점:** 판매량보다 원가 경쟁력, 배터리 기술, 충전 사업의 수익성을 봐야 합니다.