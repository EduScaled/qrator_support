from app.core.whitelist.actions import permanently, hourly, remove_whitelist, check_whitelist
from app.core.blacklist.actions import check as check_blacklist, remove_blacklist


def add_ip_address_permanently(ip_address, username):
    return permanently(ip_address, username)


def add_ip_address_hourly(ip_address, username):
    return hourly(ip_address, username)


def remove_ip_address_whitelist(ip_address, username):
    return remove_whitelist(ip_address, username)


def remove_ip_address_blacklist(ip_address, username):
    return remove_blacklist(ip_address, username)


def check_ip_whitelist(ip_address, username):
    return check_whitelist(ip_address, username)


def check_ip_blacklist(ip_address, username):
    return check_blacklist(ip_address, username)