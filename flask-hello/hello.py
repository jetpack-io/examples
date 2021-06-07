from main import app
from os import environ


@app.route('/')
def hello_world():
    return 'Hello! You are currently in {0}'.format(environ.get("FLASK_ENV"))
