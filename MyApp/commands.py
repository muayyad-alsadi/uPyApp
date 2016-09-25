# -*- coding: UTF-8 -*-

import sys, os, os.path
import logging

from .common import *

logger = logging.getLogger(__name__)

@command
def example(arg1, arg2=0):
    """
    an example command
    
    this is just a stupid example that takes two arguments and display their sum
    """
    arg1=try_int(arg1, None)
    if arg1==None:
        raise TypeError("arg1 is invalid")
    arg2=try_int(arg2, 0)
    print("sum of {}+{}={}".format(arg1,arg2, arg1+arg2))

@command
def plugin_test(myarg="default"):
    """
    an example command that shows plugins
    
    read plugin class from plugin-example section in my-app.ini
    """
    klass=app_config.opt_string("plugin-example", "class")
    if klass.startswith('.'): klass='MyApp.MyPlugins'+klass
    plugin=factory(klass+'.Plugin', myarg)
    plugin.do_it()


@command
def serve(port=8080, host='127.0.0.1', debug=None, server='flask'):
    """
    run web server
    
    server=flask,paste
    debug='0' or '1' defaults to 1 if log-level==debug
    see:
    * http://flask.pocoo.org/docs/0.11/api/#flask.Flask.run
    * http://werkzeug.pocoo.org/docs/0.11/serving/
    """
    from .web import app
    if debug==None:
        debug= app_config.is_debug
    else:
        debug=True if debug=='1' else False
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    if server=='flask':
        app.run(host=host, port=port, debug=debug, use_reloader=debug)
    else:
        # see http://pythonpaste.org/modules/httpserver.html#paste.httpserver.serve
        from paste.httpserver import serve
        if debug: logger.warning("no auto reload in paste")
        serve(app, host=host, port=port)

