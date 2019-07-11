import requests
from settings import QRATOR_AUTH_TOKEN
from app.utils import get_qrator_url, get_request_id


def add_ip_address(ip_address):
    headers = {
        "X-Qrator-Auth": QRATOR_AUTH_TOKEN
    }
    data = {
        "id": get_request_id(),
        "method": "whitelist_append",
        "params": [ str(ip_address) ]
    }    

    r = requests.post(url=get_qrator_url(), headers=headers, json=data)

    result = {
        "status": r.status_code,
        "json": r.json()
    }

    return result