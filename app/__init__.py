from flask import Flask
from flask_bootstrap import Bootstrap
from settings import FLASK_SECRET_KEY


app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
bootstrap = Bootstrap(app)

from app import routes