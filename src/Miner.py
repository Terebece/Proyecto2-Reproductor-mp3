import eyed3
import os.path, os
import threading
import time
from pathlib import Path
import Genres
import Rolas
from Dao import Dao

class Miner():
    '''Clase Miner que nos ayuda a leer las etiquetas de la rola.'''
    path = str(Path.home().resolve()) + "/Music"
    rolas = []
    total = 0
    iterador = None

    def __init__(self):
        self.files = os.walk(self.path)
        self.runMiner()
        read = threading.Thread(target = self.readTags)
        read.daemon = True
        read.start()

    def runMiner(self):
        '''Funcion que hace que el programa se ejecute.'''
        self.readDirectory()
        total = len(self.rolas)
        sorted(self.rolas, key = self.cmpToKey(self.comperRolas))

    def readDirectory(rolas):
        '''Funcion que lee el directorio y va agregando los archivos mp3'''
        for root, albums, songs in files:
            for rola in songs:
                (name, extension) = os.path.splitext(rola)
                if extension == ".mp3":
                    rolas.append(name + extension)
        print(rolas)

    def cmpToKey(self, cmp):
        '''Funcion que combierte a cmp a una llave'''
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
        '''Funcion que compara las rutas de dos rolas.'''
        if os.path.abspath(rola1) < os.path.abspath(rola2):
                return -1
        if os.path.abspath(rola1) > os.path.abspath(rola2):
                return 1
        return 0

    def readTags(self):
        '''Funcion que lee las etiquetas de todas las rolas que se encuentren.'''
        if total > 0:
            iterador = iter(self.rolas)
            while True:
                try:                
                    self.readRola(iterador.__next__())
                except StopIteration:
                    break

    def readRola(self, song):
        '''Funcion auxiliar que lee las etiquetas de la rola y la envia a la base de datos.'''
        pathRola = self.path + "/" + song
        tags = eyed3.load(pathRola).tag

        if len(tags) == 0:
            return

        rola = Rola.Rola(path)

        if tags.artist != None:
            rola.setPerformer(tags.artist)
        else:
            rola.setPerformer("Unknown")

        if tags.title != None:
            rola.setTitle(tags.title)
        else:
            rola.setTitle("Unknown")

        if tags.album != None:
            rola.setAlbum(album)
        else:
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
            else:
                track = int(tags.track_num)
            rola.setTrack(track)

        if tags.genre != -1:
            genre = Genres.Genres().getStringGenre(tags.genre)
            rola.setGenre(genre)

        Dao.insertRola(rola)
c = Miner()
