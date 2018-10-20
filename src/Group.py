class Group():

    def __init__(self, name):
        '''Constructor  que inicializa un grupo apartir del nombre.'''
        self.name = name
        self.startDate = ""
        self.endDate = ""
        self.integrants = []

    def getName(self):
        '''Función que regresa el nombre del grupo.'''
        return self.name

    def getStarDate(self):
        '''Función que regresa la fecha de comienzo del grupo.'''
        return self.startDate

    def getEndDate(self):
        '''Función que regresa la fecha en la que el grupo termino.'''
        return self.endDate

    def getIntegrants(self):
        '''Función que regresa los integrantes del grupo.'''
        return self.getString(self.integrants)

    def setName(self, name):
        '''Función que modificá el nombre del grupo.'''
        self.name = name

    def setStarDate(self, startDate):
        '''Función que modificá la fecha de comienzo  del grupo.'''
        self.startDate = startDate

    def setEndDate(self, endDate):
        '''Función que modificá la fecha en la que el grupo termino.''' 
        self.endDate = endDate
