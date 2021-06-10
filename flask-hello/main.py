from flask import Flask
from os import environ

# Import our routes and application code
# Declare a variable "app" with the Flask app
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello! You are currently in {0}'.format(environ.get("FLASK_ENV"))
