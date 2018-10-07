import os
import Minero

class Miner():

    path = "/Users/teresabecerril/Music"
    rolas = []
    total = 0
    iterador = None

    def direc(self):
        lstDir = os.walk(path)
        for root, albums, songs in lstDir:
            for r in songs:
                (nameRola, extension) = os.path.splitext(r)
                if extension == ".mp3":
                    self.rolas.append(nameRola+extension)
        total = len(self.rolas)
        sorted(self.rolas, key = cmpToKey(comperRola))
        self.run()

    def cmpToKey(cmp):
        'Convert a cmp= function into a key= function'
        class K:
            def __init__(self, rola, *args):
                self.rola = rola
            def __lt__(self, other):
                return cmp(self.rola, other.rola) < 0
            def __gt__(self, other):
                return cmp(self.rola, other.rola) > 0
            def __eq__(self, other):
                return cmp(self.rola, other.rola) == 0
            def __le__(self, other):
                return cmp(self.rola, other.rola) <= 0
            def __ge__(self, other):
                return cmp(self.rola, other.rola) >= 0
            def __ne__(self, other):
                return cmp(self.rola, other.rola) != 0
    return K

    def comperRola(self, rola1, rola2):
        if (os.path.abspath(a) < os.path.abspath(b))
                return -1;
        if (os.path.abspath(a) > os.path.abspath(b))
                return 1;
        return 0

    def run():
        if total > 0:
            iterador = iter(self.rolas)
            try:
                while True:
                    minero = Minero.Minero()
            except StopIteration:
                break
