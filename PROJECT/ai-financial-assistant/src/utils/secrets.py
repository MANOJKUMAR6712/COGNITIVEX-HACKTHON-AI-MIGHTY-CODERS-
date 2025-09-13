from dotenv import load_dotenv
import os

load_dotenv()

# API keys and sensitive information
WATSON_API_KEY = os.getenv("WATSON_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
GRANITE_API_KEY = os.getenv("GRANITE_API_KEY")

def get_watson_api_key():
    return WATSON_API_KEY

def get_huggingface_api_key():
    return HUGGINGFACE_API_KEY

def get_granite_api_key():
    return GRANITE_API_KEY