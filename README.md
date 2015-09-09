Feed Cleaner
============

Reads, cleans and serves feeds.

Sometimes we get feeds with Unicode characters because users copy and paste from other documents. This app serves as a feed proxy to clean up characters in bad source feeds.

For instance, if this app were deployed to `feedcleaner.example.org` and `SOURCE_DOMAIN='http://cdn-api.ooyala.com'` were set in `.env`, a request to `feedcleaner.example.org/feed1234` would clean up a feed from `cdn-api.ooyala.com/feed1234`.

## Architecture

* [Flask](http://flask.pocoo.org/) to register and serve routes.
* [Requests](http://www.python-requests.org/en/latest/) to fetch the remote feed.
* [Unidecode](https://pypi.python.org/pypi/Unidecode) to decode unicode characters.

## Setup

After cloning this repo, use virtualenvwrapper to install dependencies: `mkvirtualenv feed-cleaner --python=/usr/local/bin/python3.4 -r requirements.txt`

In a `.env` file, you'll need to set a `SOURCE_DOMAIN` variable. The app will proxy the request route to this domain to fetch the original feed.

```
SOURCE_DOMAIN='http://cdn-api.ooyala.com'
```

Run the webserver with Flask by calling `python app.py`
