import requests
from api.config import settings

def states_accessor():
    # go through the doc api examples!
    url = f"{ROOT_URL}/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())


def tracks_accessor():
    url = f"{ROOT_URL}/tracks/all/"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())