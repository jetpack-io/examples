from main import app
import os

@app.route('/')
def hello_world():
    return 'Hello, World! You are currently in {0}'.format(os.environ.get("FLASK_ENV"))
