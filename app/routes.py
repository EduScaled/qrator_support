from app import app
from flask import render_template, request, redirect, session
from app.auth import requires_auth
from app.services import add_ip_address


@app.route('/ip/add/', methods=['GET', 'POST'])
def ip_address():
    if request.method == 'POST':
        ip_address = request.form.get("ip_address", None)
        if ip_address:
            result = add_ip_address(ip_address)
            session["qrator"] = result
            return redirect("/ip/status/")

    
    return render_template('add_ip_address.html')



@app.route('/ip/status/')
@requires_auth
def status():
    result = session.get('qrator', {})
    if session.get('qrator', None):
        del session['qrator']

    return render_template('status.html', result=result)