import os
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI

from django.shortcuts import render
from django.http import JsonResponse


# .env 파일 불러오기
BASE_DIR = Path(__file__).resolve().parent.parent
envFile = BASE_DIR / '.env'

load_dotenv(envFile)
api_key = os.getenv('open_ai_key')


def chatbot(request):

    # GET 요청: 챗봇 페이지 보여주기
    if request.method == 'GET':
        # 새로운 대화 시작
        request.session['chat_history'] = []
        return render(request, 'chatbot.html')


    # POST 요청: 사용자의 질문 받아오기
    if request.method == 'POST':
        txt_input = request.POST.get('message', '').strip()

        if not txt_input:
            return JsonResponse({
                'error': '질문을 입력해주세요.'
            }, status=400)

        try:
            client = OpenAI(api_key=api_key)

            # 기존 대화 기록 불러오기
            history = request.session.get('chat_history', [])

            # 사용자 질문 추가
            history.append({
                'role': 'user',
                'content': txt_input
            })

            # OpenAI API 연결
            response = client.responses.create(
                model='gpt-5.6',

                instructions="""
                    당신은 친절한 여행 전문 챗봇입니다.
                    사용자의 여행 관련 질문에 답변해주세요.
                    여행지, 숙소, 음식, 교통편 등을 추천해주세요.
                    이전 대화 내용을 참고하여 답변해주세요.
                    누구나 이해하기 쉽게 작성해주세요.
                    확인되지 않은 정보는 단정하지 마세요.
                    마크다운 기호는 사용하지 마세요.
                """,

                input=history,
                max_output_tokens=3000,
            )

            result = response.output_text.strip()

            if not result:
                raise ValueError('API 응답이 비어 있습니다.')

            # AI 답변을 대화 기록에 추가
            history.append({
                'role': 'assistant',
                'content': result
            })

            # 최근 20개 메시지를 세션에 저장
            request.session['chat_history'] = history[-20:]

            # HTML에 답변 전달
            return JsonResponse({
                'answer': result
            })

        except (openai.OpenAIError, ValueError) as error:

            print('오류 종류:', type(error).__name__)
            print('오류 내용:', str(error))

            return JsonResponse({
                'error': 'AI 답변 생성에 실패했습니다.'
            }, status=500)

    return JsonResponse({
        'error': '지원하지 않는 요청입니다.'
    }, status=405)