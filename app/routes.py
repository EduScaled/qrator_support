from app import app
from flask import render_template, request, redirect, session
from app.auth import requires_auth
from app.services import add_ip_address_permanently, add_ip_address_hourly, \
    remove_ip_address_whitelist, check_ip_whitelist, check_ip_blacklist, remove_ip_address_blacklist


def common(request, func):
    if request.method == 'POST':
        ip_address = request.form.get("ip_address", None)
        if ip_address:
            session["qrator"] = func(ip_address, request.authorization.get('username'))
            return redirect("/ip/status/")

    return render_template('ip_address.html')


@app.route('/')
@requires_auth
def index():
    return render_template('index.html')


@app.route('/ip/add/hourly/', methods=['GET', 'POST'])
@requires_auth
def ip_address_hourly():
    return common(request, add_ip_address_hourly)


@app.route('/ip/add/permanently/', methods=['GET', 'POST'])
@requires_auth
def ip_address_permanently():
    return common(request, add_ip_address_permanently)


@app.route('/ip/remove/whitelist/', methods=['GET', 'POST'])
@requires_auth
def ip_address_remove_whitelist():
    return common(request, remove_ip_address_whitelist)


@app.route('/ip/remove/blacklist/', methods=['GET', 'POST'])
@requires_auth
def ip_remove_blacklist():
    return common(request, remove_ip_address_blacklist)


@app.route('/ip/check/whitelist/', methods=['GET', 'POST'])
@requires_auth
def ip_check_whitelist():
    return common(request, check_ip_whitelist)


@app.route('/ip/check/blacklist/', methods=['GET', 'POST'])
@requires_auth
def ip_check_blacklist():
    return common(request, check_ip_blacklist)


@app.route('/ip/status/')
@requires_auth
def status():
    result = session.get('qrator', {})
    if session.get('qrator', None):
        del session['qrator']

    return render_template('status.html', result=result)