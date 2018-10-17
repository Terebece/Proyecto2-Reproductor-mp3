class Person():

    tipos = ["Autor", "Compositor", "Cantante", "Integrante de grupo", "Cantautor", "DJ"]

    def __init__(self, stageName):
        self.stageName = stageName
        self.realName = ""
        self.birthDate = ""
        self.deathDate = ""
        self.occupation = ""

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

    def setStageName(self, stageName):
        self.stageName = stageName

    def setRealName(self, realName):
        self.realName = realName

    def setBirthDate(self, birthDate):
        self.birthDate = birthDate
