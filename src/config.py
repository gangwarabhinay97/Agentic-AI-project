import os
from dotenv import load_dotenv
load_dotenv()
class AppConfig:
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')
    MODEL_NAME = os.getenv('MODEL_NAME', 'gemini-1.5-pro')
    MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))
    OUTPUT_DIR = 'outputs'
