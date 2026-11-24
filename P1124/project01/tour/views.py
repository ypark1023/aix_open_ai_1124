import os
import json
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI
from django.shortcuts import render, redirect
from django.http import JsonResponse


# .env 파일 불러오기
BASE_DIR = Path(__file__).resolve().parent.parent
envFile = BASE_DIR / '.env'

load_dotenv(envFile)
api_key = os.getenv('open_ai_key')

# 오류 확인용
print('env 파일 경로:', envFile)
print('env 파일 존재 여부:', envFile.exists())
print('API 키 존재 여부:', bool(api_key))



def tour(request):

    # GET 요청: 결과 페이지 먼저 보여주기
    if request.method == 'GET':

        txt_input = request.GET.get('destination', '').strip()

        if not txt_input:
            return redirect('home')

        return render(request, 'tour.html', {
            'destination': txt_input,
        })


    # POST 요청: AJAX를 통해 API 호출
    if request.method == 'POST':

        txt_input = request.POST.get('destination', '').strip()

        if not txt_input:
            return JsonResponse({
                'error': '여행지를 입력해주세요.'
            }, status=400)

        try:
            client = OpenAI(api_key=api_key)

            response = client.responses.create(
                model='gpt-5.6',

                instructions="""
                    당신은 여행 설계 전문가입니다.
                    1박 2일 여행 일정을 설계해주세요.
                    여행자는 기차와 대중교통을 이용합니다.

                    다음 순서로 답변해주세요.

                    한눈에 보는 여행 일정
                    ===
                    여행지 설명
                    ===
                    숙소 추천
                    ===
                    식사 추천

                    각 항목 사이에 ===를 넣어주세요.
                    구분자는 총 3번만 사용해주세요.
                    항목 제목은 반복하지 마세요.
                    마크다운 기호는 사용하지 마세요.
                """,

                input=f'{txt_input}의 1박 2일 여행을 설계해주세요',

                max_output_tokens=3000,
            )

            result = response.output_text.strip()

            if not result:
                raise ValueError('API 응답이 비어 있습니다.')

            parts = result.split('===')

            if len(parts) == 4:

                return JsonResponse({
                    'schedule': parts[0].strip(),
                    'places': parts[1].strip(),
                    'hotels': parts[2].strip(),
                    'foods': parts[3].strip(),
                })

            else:

                return JsonResponse({
                    'schedule': result,
                    'places': '',
                    'hotels': '',
                    'foods': '',
                })

        except (openai.OpenAIError, ValueError) as error:

            print('오류 종류:', type(error).__name__)
            print('오류 내용:', str(error))

            return JsonResponse({
                'error': '여행 일정 생성에 실패했습니다.'
            }, status=500)

    return JsonResponse({
        'error': '지원하지 않는 요청입니다.'
    }, status=405)




# ########## 버전 2 ##########

# def tour(request):

#     if request.method != 'POST':
#         return redirect('index.html')

#     txt_input = request.POST.get('destination', '').strip()

#     if not txt_input:
#         return redirect('index.html')

#     try:
#         client = OpenAI(api_key=api_key)

#         response = client.responses.create(
#             model='gpt-5.6',

#             instructions="""
#                 당신은 여행 설계 전문가입니다.
#                 1박 2일 여행 일정을 설계해주세요.
#                 여행자는 기차와 대중교통을 이용합니다.

#                 답변은 반드시 다음 JSON 형식으로 작성해주세요.

#                 {
#                     "schedule": "1일차와 2일차의 전체 여행 일정",
#                     "places": "추천 여행지와 각각의 설명",
#                     "hotels": "추천 숙소와 추천 이유",
#                     "foods": "추천 음식과 식사 장소"
#                 }

#                 모든 항목은 문자열로 작성해주세요.
#                 마크다운 기호는 사용하지 마세요.
#                 확인되지 않은 가격이나 운영시간은 단정하지 마세요.
#                 누구나 이해하기 쉽게 작성해주세요.
#             """,

#             input=f'{txt_input}의 1박 2일 여행을 설계하고 JSON 형식으로 답변해주세요.',

#             text={
#                 "format": {
#                     "type": "json_object"
#                 }
#             },

#             max_output_tokens=3000,
#         )

#         # JSON 문자열을 파이썬 딕셔너리로 변환
#         result = json.loads(response.output_text)

#         # HTML로 전달할 데이터
#         context = {
#             'destination': txt_input,
#             'schedule': result['schedule'],
#             'places': result['places'],
#             'hotels': result['hotels'],
#             'foods': result['foods'],
#         }

#     except (
#     openai.OpenAIError,
#     json.JSONDecodeError,
#     KeyError,
#     TypeError
#             ) as error:

#         print('오류 종류:', type(error).__name__)
#         print('오류 내용:', str(error))

#     context = {
#         'destination': txt_input,
#         'error': '여행 일정 생성에 실패했습니다.'
#     }

#     return render(request, 'tour.html', context)