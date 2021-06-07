from jetpack import cron
from os import environ
import requests
import time

headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}
url = environ.get("SLACK_URL")


@cron.repeat(cron.every(10).minutes)
def ten_minute_job():
    payload = '{"text":"I\'m a cronjob that runs every minute"}'
    time.sleep(20)
    requests.post(url, data=payload, headers=headers)
