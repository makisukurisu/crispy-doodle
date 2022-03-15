import requests

def getJSON(url: str, *args, **kwargs):

    try:
        response = requests.get(url, *args, **kwargs)
        response_json = response.json()
        return response_json
    except requests.exceptions.JSONDecodeError:
        return None
        #or raise
    except Exception as E:
        raise E