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

    def getGroup(self):
        return self.group

    def getSongs(self):
        return self.songs

    def setName(self, name):
        self.name = name

    def setYear(self, year):
        self.year = year

    def setGroup(self, group):
        self.group = group

    def setGenre(self, genre):
        self.genre = genre

    def addSong(self, song):
        self.songs.append(song)
