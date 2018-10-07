from tagger import *
import Genres
import os

class Minero():

    path = "/Users/teresabecerril/Music"
    lstFiles = []

    def __init__(self):
        self.readTags()

    def direc(self):
        lstDir = os.walk(path)
        for root, albums, rolas in lstDir:
            for rola in rolas:
                (nameRola, extension) = os.path.splitext(rola)
                if(extension == ".mp3"):
                    lstFiles.append(nameRola+extension)

    def readTags(self):
