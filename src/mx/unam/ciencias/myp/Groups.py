class Groups():

    def __init__(self, identifier):
        self.identifier = identifier
        self.name = ""
        self.startDate = ""
        self.endDate = ""

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
