import sys
import time
import signal
import logging

try: import simplejson as json
except ImportError: import json

from flask import Flask

from .common import *

logger = logging.getLogger(__name__)

application = app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong@'+str(time.time())

def main():
    """
    see:
    * http://flask.pocoo.org/docs/0.11/api/#flask.Flask.run
    * http://werkzeug.pocoo.org/docs/0.11/serving/
    """
    app.run(host='0.0.0.0', port=8080, debug=app_config.is_debug, use_reloader=app_config.is_debug)

if __name__ == '__main__':
    main()

