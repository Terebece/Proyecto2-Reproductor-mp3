import eyed3
import os.path
import os
import threading
import time
import Genres
import Rolas

class Miner():

    path = "/Users/teresabecerril/Music"
    rolas = []
    total = 0
    iterador = None
    Rolas =[]

    def __init__(self):
        files = os.walk(path)
        self.runMiner()
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
        performer = title = album = None
        year = track = genre = total = -1
        artPicture = albPicuture = None

        path = os.path.abspath(song)
        rola = Rola.Rola(path)
        tags = eyed3.load(path).tag

        if len(tags) == 0:
            return

        if tags.artist != None:
            performer = tags.artist
            rola.setPerformer(performer)

        if tags.title != None:
            title = tags.title
            rola.setTitle(title)

        if tags.album != None:
            album = tags.album
            rola.setAlbum(album)

        if tags.year != -1:
            year = tags.year
            rola.setYear(year)

        if tags.track_num != None:
            if tags.track_num.find("/") != -1:
                trackNum = tags.track_num.split("/")
                track = int(trackNum[0])
            else:
                track = int(tags.track_num)
            rola.setTrack(track)

        if tags.genre != -1:
            genres = Genre.Genre()
            genre = genres.gentStringGenre(tags.genre)
            rola.setGenre(genre)
