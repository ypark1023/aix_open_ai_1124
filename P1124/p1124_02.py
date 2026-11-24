import os
from dotenv import load_dotenv
import openai
from openai import OpenAI

# .env 파일 불러오기
load_dotenv()
api_key = os.getenv('open_ai_key')

# API 키 로딩 확인
print('API 키 확인:', bool(api_key))
client = OpenAI(api_key=api_key)

try:
    print('API 연결을 시작합니다.')

    response = client.responses.create(
        model='gpt-5.6',
        instructions='한국어로 친절하고 간결하게 답변해주세요',
        input='api 연결확인 문자를 15자내로 짧게 작성해주세요'
    )

    # API 응답 출력
    print(response.output_text)

except openai.APIConnectionError as error:
    print(f'api 연결에러 발생: {error}')

except openai.RateLimitError as error:
    print(f'api 요청한도에러 발생: {error}')

except openai.APIError as error:
    print(f'api 요청 실패: {error}')


result = response.output_text.strip()
if not result :
    raise RuntimeError('api 응답에 표시할 텍스트 없음')
print('-'*40)
print(response)
print('-'*40)
print(result)