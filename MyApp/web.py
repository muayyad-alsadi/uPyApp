import sys
import time
import signal
import logging

try: import simplejson as json
except ImportError: import json

from bottle import Bottle, request, run, response

from .common import *

logger = logging.getLogger(__name__)

application = app = Bottle()


@app.get('/ping')
def ping():
    return 'pong@'+str(time.time())

def main():
    run(app, host='localhost', port=8800,  debug=True)

if __name__ == '__main__':
    main()

