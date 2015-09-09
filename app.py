import os
import requests
from flask import Flask
from flask import request
from flask import Response
from honcho import environ


app = Flask(__name__)


def update_env(filename='.env'):
    """
    Update os.environ with variables from an .env file.

    Parameters:
        filename (Optional[str]): the name of the .env file. Defaults to '.env'.
    """
    with open(filename) as f:
        content = f.read()
    envvars = environ.parse(content)

    for k, v in envvars.items():
        os.environ[k] = v


@app.route('/')
def index():
    return 'This app cleans the feeds its been given.'


@app.route('/<path:path>')
def read_clean_feed(path):
    feed_url = "%s/%s" % (os.getenv('SOURCE_DOMAIN'), path)
    if request.query_string:
        feed_url += '?' + request.query_string
    feed_resp = requests.get(feed_url)
    flask_resp = Response(feed_resp.content)
    flask_resp.headers['content-type'] = feed_resp.headers['content-type']
    return flask_resp


if __name__ == "__main__":
    update_env()
    app.run()
