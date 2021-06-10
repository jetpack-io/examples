from jetpack import cron
from os import environ
from flask import Flask
import requests
import time

app = Flask(__name__)

headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}
url = environ.get("SLACK_URL")


@cron.repeat(cron.every(10).minutes)
def cron_job_ten():
    payload = '{"text":"I\'m a cronjob that runs every 10 minutes"}'
    time.sleep(20)
    requests.post(url, data=payload, headers=headers)
