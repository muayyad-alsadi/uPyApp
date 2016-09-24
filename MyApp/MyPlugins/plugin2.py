class Plugin(object):
    def __init__(self, myarg):
        self.myarg = myarg
    def do_it(self):
        print("plugin2: doing it with myarg={}".format(self.myarg))
