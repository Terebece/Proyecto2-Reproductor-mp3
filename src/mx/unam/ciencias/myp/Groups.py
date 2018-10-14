class Groups():

    def __init__(self, name):
        self.name = name
        self.startDate = ""
        self.endDate = ""
        self.genre = ""
        self.integrants = []
        self.songs = []

    def getName(self):
        return self.name

    def getStarDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def getIntegrants(self):
        return self.getString(self.integrants)

    def getSongs(self):
        return self.songs 

    def getGenre(self):
        return self.genre

    def getString(self, lista):
        obt = ""
        i = 0
        for elem in lista:
            if lista[i] == elem:
                if(i == (len(lista)-1)):
                    obt = obt + elem
                else:
                    obt = obt + elem + ", "
                i += 1
        return obt

    def setName(self, name):
        self.name = name

    def setStarDate(self, startDate):
        self.startDate = startDate

    def setEndDate(self, endDate):
        self.endDate = endDate

    def setGenre(self, genre):
        self.genre = genre

    def addIntegrant(self, integrant):
        self.integrants.append(integrant)

    def addSong(self, song):
        self.songs.append(song)
