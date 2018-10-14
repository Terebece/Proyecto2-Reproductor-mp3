class Albums():

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.year = 0
        self.performer = ""
        self.songs = []

    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

    def getPerformer(self):
        return self.performer

    def getSongs(self):
        return self.songs

    def setName(self, name):
        self.name = name

    def setYear(self, year):
        self.year = year

    def setPerformer(self, artist):
        self.performer = artist

    def addSong(self, song):
        self.songs.append(song)
