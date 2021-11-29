import requests
import json


def get_secret(secret_name: str):
    with open('secrets.json') as handle:
        data = json.load(handle)
        try:
            ret: str = data[secret_name]
            return ret
        except KeyError:
            return None


channel = get_secret('channel')
payload = {'text': 'Hello, World!'}
r = requests.post(
    channel,
    data=json.dumps(payload),
)