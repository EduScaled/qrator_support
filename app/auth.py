from functools import wraps
from flask import request, Response
from settings import BASIC_AUTH


def check_auth(username, password):
    for account in BASIC_AUTH.split(";"):
        credentials = account.split(":")
        if username == credentials[0] and password == credentials[1]:
            return True

    return False


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated