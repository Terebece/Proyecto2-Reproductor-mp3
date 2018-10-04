class Albums():

    def __init__(self, identifier, path):
        self.identifier = identifier
        self.path = path
        self.name = ""
        self.year = 0
        self.genre = ""
        self.group = ""
        self.songs = []

    def getIdentifier(self):
        return self.identifier

    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

    def setName(self, name):
        self.name = name

    def setYear(self, year):
        self.year = year

    def getGenre(self):
        return self.genre

    def getGroup(self):
        return self.group

    def getSongs(self):
        return self.songs

    def setGroup(self, group):
        self.group = group

    def addSong(self, song):
        self.songs.append(song)

    def setGenre(self, genre):
        self.genre = genre
