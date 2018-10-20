import sqlite3
import Rola
import Group
import Person
from DataBase import DataBase

class Dao():

    def __init__(self):
        c = DataBase.getCursor()

    def getArtist(self, a):
        c.execute('''SELECT * FROM rolas WHERE performers(id_album) LIKE '%a%' ''')

    def getAlbum(self, a):
        c.execute('''SELECT * FROM rolas WHERE albums(id_performer) LIKE '%a%' ''')

    def getTitle(self, t):
        c.execute('''SELECT * FROM rolas WHERE title LIKE '%t%' ''')

    def getGenre(self, g):
        c.execute('''SELECT * FROM rolas WHERE genre LIKE '%g%' ''')

    def getYear(self, y):
        c.execute('''SELECT * FROM rolas WHERE year LIKE '%y%' ''')
        
    def insertRola(self, rola):
        path = rola.getPath()
        title = rola.getTitle()
        year = rola.getYear()
        track = rola.getTrack()
        genre = rola.getGenre()
        c.execute('''INSERT INTO rolas VALUES(null, path, title, year, track, genre, null, null)''')
        
    def insertPerson(self, person):
        stage = person.getStageName()
        real = person.getRealName()
        birth = person.getBirthDate()
        death = person.getDeathDate()
        c.execute('''INSERT INTO persons VALUES(null, stage, real, birth, death)''')
        
    def insertGroup(self, group):
        name = group.getName()
        start = group.getStarDate()
        end = group.getEndDate()
        c.execute('''INSERT INTO groups VALUES(null, name, start, end)''')
