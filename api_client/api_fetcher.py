from requests import get
import logging


def fetch(url):
    response = get(url)
    data = response.json()
    logging.basicConfig(level=logging.INFO)
    if response.status_code == 200:
        # logging.info(response.text)
        return dict({'id': data['id'], 'quote': data['quote'], 'status_code': response.status_code})
    else:
        logging.debug(response.text)
        return dict(
            {'id': data['id'], 'quote': data['quote'], 'status_code': response.status_code, 'text': response.text})
