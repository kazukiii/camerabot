import os
import subprocess

from slackbot.bot import listen_to
import requests

@listen_to('now')
def listen_func(message):
    subprocess.call('raspistill -o image.jpg', shell=True)

    TOKEN = os.environ.get('API_TOKEN')
    ImagePath = './image.jpg'

    CHANNEL = os.environ.get('CHANNEL')
    FILENAME = 'my_file'
    files = {'file': open(ImagePath, 'rb')}
    param = {
        'token': TOKEN,
        'channels': CHANNEL,
        'filename': FILENAME,
    }

    requests.post(url="https://slack.com/api/files.upload", params=param, files=files)
