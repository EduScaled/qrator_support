import requests
from app.helpers.qrator import get_qrator_url, get_request_id, get_qrator_headers


def hourly(ip_address):
    data = {
        "id": get_request_id(),
        "method": "whitelist_append",
        "params": [ [ str(ip_address), 3600] ]
    }    

    r = requests.post(url=get_qrator_url(), headers=get_qrator_headers(), json=data)

    result = {
        "status": r.status_code,
        "message": "IP successfully HOURLY ADDED to WHITELIST!",
        "ip_address": ip_address,
        "json": r.json()
    }

    return result


def permanently(ip_address):
    data = {
        "id": get_request_id(),
        "method": "whitelist_append",
        "params": [ str(ip_address) ]
    }    

    r = requests.post(url=get_qrator_url(), headers=get_qrator_headers(), json=data)

    result = {
        "status": r.status_code,
        "message": "IP successfully PERMANENTLY ADDED to WHITELIST!",
        "ip_address": ip_address,
        "json": r.json()
    }

    return result


def remove_whitelist(ip_address):
    data = {
        "id": get_request_id(),
        "method": "whitelist_remove",
        "params": [ str(ip_address) ]
    }    

    r = requests.post(url=get_qrator_url(), headers=get_qrator_headers(), json=data)

    result = {
        "status": r.status_code,
        "message": "IP successfully REMOVED FROM WHITELIST!",
        "ip_address": ip_address,
        "json": r.json()
    }

    return result


def check_whitelist(ip_address):

    data = {
        "id": get_request_id(),
        "method": "whitelist_get",
        "params": [ str(ip_address) ]
    }    

    r = requests.post(url=get_qrator_url(), headers=get_qrator_headers(), json=data)

    json = r.json()

    in_list = False
    for ip in json.get('result', None):
        if (isinstance(ip, str) and ip == str(ip_address)) or \
            (isinstance(ip, list) and ip[0] == str(ip_address)):
                in_list = True

    result = {
        "status": r.status_code,
        "message": f'IP {ip_address} IN WHITELIST' if in_list else f'IP {ip_address} IS NOT IN WHITELIST',
        "ip_address": ip_address,
        "json": json
    }

    return result