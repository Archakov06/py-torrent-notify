import requests
import re
import sys
import threading
from requests.auth import HTTPBasicAuth

if len(sys.argv) == 1:
    print('Please, set your bot token!')
    exit()

USER = '1'
PASSWORD = '1'
PORT = 9999
TOKEN = sys.argv[1]
URL = 'http://localhost:' + str(PORT)

downloadedTorrents = []


def setInterval(func, sec):
    t = threading.Timer(sec, func)
    t.start()


def getTorrents():
    r = requests.get(URL + '/gui/?list=1', auth=HTTPBasicAuth(USER, PASSWORD))
    data = r.json()['torrents']
    return data


def serializeTorrentInfo(arr):
    return {
        "hash": arr[0],
        "name": arr[2],
        "size": arr[3],
        "percent": float(arr[4]) / 10,
        "downloaded": arr[5],
        "peers": arr[13],
        "seeds": arr[15],
        "position": arr[17],
        "status": arr[21]
    }


def notifyMe(torrent):
    global downloadedTorrents
    downloadedTorrents.append(torrent['hash'])
    URL = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage'
    DATA = {
        "chat_id": 129070250,
        "text": "Загрузка торрента \"*{0}*\" завершена!".format(torrent['name']),
        "parse_mode": "Markdown"
    }
    requests.post(url=URL, data=DATA)


def start():
    print('started')
    torrentsArray = getTorrents()
    for obj in torrentsArray:
        torrent = serializeTorrentInfo(obj)
        if not torrent['hash'] in downloadedTorrents and torrent['percent'] == 100:
            notifyMe(torrent)
    setInterval(start, 3)


start()
