import logging
import shelve

api = {
    'url': 'https://io-stabcode-tweet-bot.herokuapp.com/quotes/',
    'current_id': 1,
    'total_id': 298
}

db = shelve.open('props.db')

try:
    props = db['api']
except KeyError:
    db['api'] = api
    props = db['api']
finally:
    db.close()

logging.basicConfig(level=logging.INFO)


def get_url():
    return props['url'] + str(props['current_id'])


def update_props(id):
    with shelve.open('props.db') as db:
        try:
            data = db['api']
            data['current_id'] = id
            db['api'] = data
        finally:
            db.close()
