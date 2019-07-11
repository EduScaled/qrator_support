import os


DB_PATH = os.getenv("DB_PATH")
BASIC_AUTH = os.getenv("BASIC_AUTH")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
QRATOR_URL = os.getenv("QRATOR_URL", "https://api.qrator.net/request/domain/")
QRATOR_DOMAIN_ID = os.getenv("QRATOR_DOMAIN_ID") 
QRATOR_AUTH_TOKEN = os.getenv("QRATOR_AUTH_TOKEN")