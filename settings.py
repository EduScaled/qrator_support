import os


BASIC_AUTH_LOGIN = os.getenv("BASIC_AUTH_LOGIN", "admin")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "secret")

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "secret_key")

QRATOR_URL = os.getenv("QRATOR_URL", "https://api.qrator.net/request/domain/")
QRATOR_DOMAIN_ID = os.getenv("QRATOR_DOMAIN_ID") 
QRATOR_AUTH_TOKEN = os.getenv("QRATOR_AUTH_TOKEN")

