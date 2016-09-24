class Plugin(object):
    def __init__(self, myarg):
        self.myarg = myarg
    def do_it(self):
        print("doing it with myarg={} inside plugin1".format(self.myarg))
