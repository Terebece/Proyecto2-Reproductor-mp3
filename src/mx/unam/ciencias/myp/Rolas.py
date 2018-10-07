class Rolas():

    def __init__(self):
        self.title = None
        self.performer = None
        self.album = None
        self.year = 0
        self.track = 0
        self.genre = None
        self.picture = None

    def getTitle(self):
        return self.title

    def getPerformer(self):
        return self.performer

    def getAlbum(self):
        return self.album

    def getYear(self):
        return self.year

    def getTrack(self):
        return self.track

    def getGenre(self):
        return self.genre

    def getPicture(self):
        return self.picture

    def setTitle(self, title):
        self.title = title

    def setPerformer(self, performer):
        self.performer = performer

    def setAlbum(self, album):
        self.album = album

    def setYear(self, year):
        self.year = year

    def setTrack(self, track):
        self.track = track

    def setGenre(self, genre):
        self.genre = genre

    def setPicture(self, picture):
        self.picture = picture
