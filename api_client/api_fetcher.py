from requests import get


def fetch(url):
    response = get(url)
    if response.status_code == 200:
        data = response.json()
        print(data['quote'])

