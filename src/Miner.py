import eyed3
import os.path, os
import threading
import time
import Genres
import Rolas
import Dao

class Miner():

    path = "~/Music"
    rolas = []
    total = 0
    iterador = None

    def __init__(self):
        files = os.walk(path)
        self.runMiner()
        self.reproductor = Reproductor.Reproductor()
        read = threading.Thread(target = self.readTags)
        read.daemon = True
        read.start()

    def runMiner(self):
        self.readDirectory()
        total = len(self.rolas)
        sorted(self.rolas, key = cmpToKey(comperRola))

    def readDirectory(self):
        for root, albums, songs in files:
            for rola in songs:
                (name, extension) = os.path.splitext(rola)
                if extension == ".mp3":
                    rolas.append(name + extension)

    def cmpToKey(cmp):
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

    def comperRolas(self, rola1, rola2):
        if (os.path.abspath(a) < os.path.abspath(b))
                return -1;
        if (os.path.abspath(a) > os.path.abspath(b))
                return 1;
        return 0

    def readTags(self):
        if total > 0:
            iterador = iter(self.rolas)
            try:
                while True:
                    self.readRola(iterador.__next__())
            except StopIteration:
                break

    def readRola(self, song):
        path = os.path.abspath(song)
        tags = eyed3.load(path).tag

        if len(tags) == 0:
            return

        rola = Rola.Rola(path)

        if tags.artist != None:
            rola.setPerformer(tags.artist)
        elif:
            rola.setPerformer("Unknown")

        if tags.title != None:
            rola.setTitle(tags.title)
        elif:
            rola.setTitle("Unknown")

        if tags.album != None:
            rola.setAlbum(album)
        elif:
            rola.setAlbum("Unknown")

        if tags.year != 0:
            rola.setYear(int(tags.year))
        else:
            rola.setYear(time.ctime(os.path.getctime(path)))

        if tags.track_num != None:
            track = 0
            if tags.track_num.find("/") != -1:
                trackNum = tags.track_num.split("/")
                track = int(trackNum[0])
            elif
                track = int(tags.track_num)
            rola.setTrack(track)

        if tags.genre != -1:
            genre = Genres.Genres().getStringGenre(tags.genre)
            rola.setGenre(genre)

        self.Dao.insertRola(rola)
