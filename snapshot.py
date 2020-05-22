import os
import subprocess
from datetime import datetime

import requests
from pytz import timezone

subprocess.call('raspistill -o image.jpg', shell=True)

now = datetime.now().astimezone(timezone('Asia/Tokyo'))
TOKEN = os.environ.get('API_TOKEN')
ImagePath = './image.jpg'
initialComment = '{}:00'.format(now.strftime("%Y/%m/%d %H"))

CHANNEL = os.environ.get('CHANNEL')
FILENAME = 'my_file'
files = {'file': open(ImagePath, 'rb')}
param = {
    'token': TOKEN,
    'channels': CHANNEL,
    'filename': FILENAME,
    'initial_comment': initialComment,
}

requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
