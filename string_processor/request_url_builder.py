import logging
import shelve

api = {
    'url': 'https://io-stabcode-tweet-bot.herokuapp.com/quotes/',
    'current_id': 1,
    'total_id': 298
}

logging.basicConfig(level=logging.INFO)


def get_props():
    with shelve.open('props.db') as db:
        try:
            props = db['api']
        except KeyError:
            db['api'] = api
            props = db['api']
        finally:
            return props


def get_url():
    props = get_props()
    return props['url'] + str(props['current_id'])


def update_props(id):
    with shelve.open('props.db') as db:
        try:
            data = db['api']
            data['current_id'] = id
            db['api'] = data
        except KeyError:
            pass
