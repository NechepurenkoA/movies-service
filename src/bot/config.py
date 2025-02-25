import os

from dotenv import load_dotenv

load_dotenv()

# BOT CONFIGS
TOKEN = os.getenv("TOKEN")
INTERNAL_API_URL = os.getenv("INTERNAL_API_URL", "http://127.0.0.1:8000/api/v1/")
SITE_URL = os.getenv("SITE_URL", "http://127.0.0.1:8000/")


# LOGGER CONFIGS
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")
LOGGING_FORMAT = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
)
