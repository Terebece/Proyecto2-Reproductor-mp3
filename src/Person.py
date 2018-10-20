class Person():

    tipos = ["Autor", "Compositor", "Cantante", "Integrante de grupo", "Cantautor", "DJ"]

    def __init__(self, stageName):
        '''Contructor que inicializa una persona apartir de su nombre artistico'''
        self.stageName = stageName
        self.realName = ""
        self.birthDate = ""
        self.deathDate = ""
        self.occupation = ""

    def getStageName(self):
        '''Función que regresa el nombre artístico de la persona.'''
        return self.stageName

    def getRealName(self):
        '''Función que regresa el nombre real de la persona.''' 
        return self.realName

    def getBirthDate(self):
        '''Función que regresa la fecha de cumpleaños de la persona.'''
        return self.birthDate

    def getDeathDate(self):
        '''Función que regresa la fecha de muerte de la persona.'''
        return self.deathDate

    def setRealName(self, realName):
        '''Función que modificá el nombre real de la persona.'''
        self.realName = realName

    def setBirthDate(self, birthDate):
        '''Función que modificá la fecha de cumpleaños de la persona'''
        self.birthDate = birthDate

    def setDeathDate(self, deathDate):
        '''Función que modificá la fecha de muerte de la persona.'''
        self.deathDate = deathDate
