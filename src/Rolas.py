class Rolas():

    def __init__(self, path):
        '''Constructor que inicializa una rola apatir de su ruta.'''
        self.path = path
        self.title = ""
        self.performer = ""
        self.album = ""
        self.year = 0
        self.track = 0
        self.genre = -1
        self.picture = None

    def getPath(self):
        '''Función que regresa la ruta de la rola.'''
        return self.path

    def getTitle(self):
        '''Función que regresa el título de la rola.'''
        return self.title

    def getPerformer(self):
        '''Función que regresa el intérprete de la rola.'''
        return self.performer

    def getAlbum(self):
        '''Función que regresa el album de la rola.'''
        return self.album

    def getYear(self):
        '''Función que regresa el año en el que salió la rola.'''
        return self.year

    def getTrack(self):
        '''Función que regresa el número de track de la rola'''
        return self.track

    def getGenre(self):
        '''Función que regrsa el género de la rola.'''
        return self.genre

    def getPicture(self):
        '''Función que regresa la imagen de la rola.'''
        return self.picture

    def setTitle(self, title):
        '''Función que modificá el título de la rola.'''
        self.title = title

    def setPerformer(self, performer):
        '''Función modificá el intérprete de la rola.'''
        self.performer = performer

    def setAlbum(self, album):
        '''Función modificá el album de la rola.'''
        self.album = album

    def setYear(self, year):
        '''Función modificá el año en el que salió la rola.'''
        self.year = year

    def setTrack(self, track):
        '''Función modificá el número de track de la rola. '''
        self.track = track

    def setGenre(self, genre):
        '''Función modificá el género de la rola. '''
        self.genre = genre

    def setPicture(self, picture):
        '''Función que modificá la imagen de la rola.'''
        self.picture = picture
