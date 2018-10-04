class Groups():

    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name
        self.startDate = ""
        self.endDate = ""
        self.genre = ""
        self.integrants = []
        self.songs = []

    def getIdentifier(self):
        return self.identifier

    def getName(self):
        return self.name

    def getStarDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def setName(self, name):
        self.name = name

    def setStarDate(self, startDate):
        self.startDate = startDate

    def setEndDate(self, endDate):
        self.endDate = endDate

    def getIntegrants(self):
        return self.integrants

    def getSongs(self):
        return self.songs

    def getGenre(self):
        return self.genre

    def addIntegrant(self, integrant):
        self.integrants.append(integrant)

    def addSong(self, song):
        self.songs.append(song)

    def setGenre(self, genre):
        self.genre = genre
