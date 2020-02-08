from api_client import api_fetcher
from string_processor import request_url_builder
from twitter_client import tweet_bot
import logging


def execute():
    try:
        url = request_url_builder.get_url()

        if url is not None:
            response = api_fetcher.fetch(url)
            if response['status_code'] == 200:
                if tweet_bot.tweet(response['quote']):
                    request_url_builder.update_props(response['id'] + 1)

    except (KeyError, RuntimeError, EnvironmentError, ConnectionError, TimeoutError):
        logging.critical("Failed to Tweet for URL:" + url + " Sending Dm")
