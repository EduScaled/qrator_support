import requests
from app.helpers.logger import log
from app.helpers.qrator import get_qrator_url, get_request_id, get_qrator_headers, get_status


def hourly(ip_address, username):
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

    log(get_status(result), "ADD_IP_FOR_HOUR_TO_WHITELIST", str(ip_address), username)

    return result


def permanently(ip_address, username):
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

    log(get_status(result), "ADD_IP_PERMANENTLY_TO_WHITELIST", str(ip_address), username)

    return result


def remove_whitelist(ip_address, username):
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

    
    log(get_status(result), "REMOVE_IP_FROM_WHITELIST", str(ip_address), username)

    return result


def check_whitelist(ip_address, username):

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

    log(get_status(result), "CHECK_IP_IN_WHITELIST", str(ip_address), username)

    return result