import requests

def check_if_url(link):
    try:
        site=requests.get(link)
        return True;
    except Exception:
        return False