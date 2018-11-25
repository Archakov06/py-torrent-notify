import requests
import re
import sys
from requests.auth import HTTPBasicAuth

if len(sys.argv) == 1:
    print('Please, set your bot token!')
    exit()

USER = '1'
PASSWORD = '1'
PORT = 9999
TOKEN = sys.argv[1]
URL = 'http://localhost:' + str(PORT)


def getTorrents():
    r = requests.get(URL + '/gui/?list=1', auth=HTTPBasicAuth(USER, PASSWORD))
    data = r.json()['torrents']
    return data


def serializeTorrentInfo(arr):
    return {
        "name": arr[2],
        "size": arr[3],
        "percent": float(arr[4]) / 10,
        "downloaded": arr[5],
        "peers": arr[13],
        "seeds": arr[15],
        "position": arr[17],
    }


def notifyMe(torrentName):
    URL = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage'
    DATA = {
        "chat_id": 129070250,
        "text": "Загрузка торрента \"*{0}*\" завершена!".format(torrentName),
        "parse_mode": "Markdown"
    }
    requests.post(url=URL, data=DATA)


obj = serializeTorrentInfo(getTorrents()[2])
notifyMe(obj['name'])
