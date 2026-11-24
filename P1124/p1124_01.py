import os
from dotenv import load_dotenv


# .env 파일 불러오기
load_dotenv()
print('api key:', os.getenv('open_ai_key'))
