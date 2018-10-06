class Albums():

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.year = 0
        self.genre = ""
        self.artist = ""
        self.songs = []

    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

    def getGenre(self):
        return self.genre

    def getArtist(self):
        return self.artist

    def getSongs(self):
        obt = ""
        i = 0
        for elem in self.songs:
            if self.songs[i] == elem:
                if(i == (len(self.songs)-1)):
                    obt = obt + elem
                else:
                    obt = obt + elem + ", "
                i += 1
        return obt

    def setName(self, name):
        self.name = name

    def setYear(self, year):
        self.year = year

    def setArtist(self, artist):
        self.artist = artist

    def setGenre(self, genre):
        self.genre = genre

    def addSong(self, song):
        self.songs.append(song)
