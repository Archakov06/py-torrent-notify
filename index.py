import requests
import re
from requests.auth import HTTPBasicAuth

USER = '1'
PASSWORD = '1'
PORT = 9999

URL = 'http://localhost:' + str(PORT)


def getTorrents():
    r = requests.get(URL + '/gui/?list=1', auth=HTTPBasicAuth(USER, PASSWORD))
    data = r.json()['torrents']
    return data


def sendMessage():
    URL = 'https://api.telegram.org/botXXX:XXX/sendMessage'
    DATA = {
        "chat_id": 129070250,
        "text": "Hello"
    }
    requests.post(url=URL, data=DATA)


sendMessage()
