import os 
from dotenv import load_dotenv

load_dotenv(override=True)

CONFIG = {
    "llm": {
        "llm_base_url": os.getenv('LITELLM_BASE_URL'),
        "llm_api_key": os.getenv('LITELLM_API_KEY')
    },
    "models": {
    "gpt": "gpt-5-mini",
    "google": "gemini-3.5-flash",
    "alibaba": "qwen3.6-27b"
    }
}