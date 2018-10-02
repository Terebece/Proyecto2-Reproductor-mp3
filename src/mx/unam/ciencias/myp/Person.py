import BandaMusical

class Person():

    tipos = ["Autor", "Compositor", "Interprete", "Integrante de ", "Cantautor", "DJ"]

    def __init__(self, identifier):
        self.identifier = identifier
        self.stageName = ""
        self.realName = ""
        self.birthDate = ""
        self.deathDate = ""
        self.occupation = ""
        self.songs = []
        self.albums = []

    def getIdentifier(self):
        return self.identifier

    def getStageName(self):
        return self.stageName

    def getRealName(self):
        return self.realName

    def getBirthDate(self):
        return self.birthDate

    def getDeathDate(self):
        return self.deathDate

    def getOccupation(self):
        return self.occupation

    def getSongs(self):
        return self.getString(self.songs)

    def getAlbums(self):
        return self.getString(self.albums)

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

    def setStageName(self, stageName):
        self.stageName = stageName

    def setRealName(self, realName):
        self.realName = realName

    def setBirthDate(self, birthDate):
        self.birthDate = birthDate

    def setDeathDate(self, deathDate):
        self.deathDate = deathDate

    def addOcuppation(self, occupation):
        if len(self.occupation) > 0:
            self.occupation = self.occupation + ", " + occupation
        else:
            self.occupation = occupation

    def addSongs(self, song):
        self.songs.append(song)

    def addAlbums(self, album):
        self.albums.append(album)
