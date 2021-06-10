from os import environ
import requests
import time

headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}
url = environ.get("SLACK_URL")

def cron_job():
    payload = '{"text":"I\'m a cronjob that runs every 10 minutes"}'
    time.sleep(20)
    requests.post(url, data=payload, headers=headers)
