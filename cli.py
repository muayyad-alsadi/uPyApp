#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os, os.path, subprocess, json

here=os.path.dirname(__file__)
if not hasattr(sys, 'real_prefix'):
    virtualenv=os.path.join(here, 'virtualenv')
    activate=os.path.join(virtualenv, 'bin','activate_this.py')
    if os.path.exists(activate):
        try: execfile(activate, {'__file__':activate})
        except IOError: pass
        sys.stderr.write("Env [%r] activated\n" % virtualenv)
    else: sys.stderr.write("activate=[%r] not found\n" % activate)

if "PyPy" in sys.version:
    ver2or3=sys.version[0]
    cmd="/usr/bin/python{} -c 'import sys, json;print(json.dumps(sys.path))'".format(ver2or3)
    out=subprocess.check_output(cmd, shell=True).strip()
    paths=json.loads(out.decode('UTF-8'))
    for path in paths:
        if path not in sys.path: sys.path.append(path)

from MyApp import cli

cli.main()
