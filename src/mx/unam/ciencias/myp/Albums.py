class Albums():

    def __init__(self, identifier):
        self.identifier = identifier
        self.path = ""
        self.name = ""
        self.year = 0

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
