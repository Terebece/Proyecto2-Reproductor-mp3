class Group():

    def __init__(self, name):
        self.name = name
        self.startDate = ""
        self.endDate = ""
        self.integrants = []

    def getName(self):
        return self.name

    def getStarDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def getIntegrants(self):
        return self.getString(self.integrants)

    def setName(self, name):
        self.name = name

    def setStarDate(self, startDate):
        self.startDate = startDate

    def setEndDate(self, endDate):
        self.endDate = endDate
