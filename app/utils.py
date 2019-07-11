import random
from settings import QRATOR_URL, QRATOR_DOMAIN_ID


def get_request_id():
    return random.randint(100,1000)


def get_qrator_url():
    return f"{QRATOR_URL}{QRATOR_DOMAIN_ID}"