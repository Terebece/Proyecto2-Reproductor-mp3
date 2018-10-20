import sqlite3
import os.path
import os

class DataBase():

    def __init__(self):
        '''Se conecta con la base de datos.'''
        self.bd = sqlite3.connect("Reproductor.db")
        self.cursor = self.bd.cursor()

    def getCursor(self):
        '''Funcion que regresa el cursor'''
        return self.cursor

    def runDb(self):
        '''Funcion donde se crean todas las tablas, guarda y cierra la base de datos'''
        self.creatTable()
        self.save()
        self.closeConnection()

    def creaTables(self):
        '''Funcion que manda a llamar a las funciones que crean todas las tablas'''
        self.creaTypesTable()
        self.insertValue()
        self.creatPerformesTable()
        self.creatPersonsTable()
        self.creatGroupsTable()
        self.creatAlbumsTable()
        self.creatRolasTable()
        self.creatInGroupTable()

    def save(self):
        '''Funcion para guardar los cambios en la base de datos'''
        self.bd.commit()

    def closeConnection(self):
        '''Funcion que cierra la conexion con la base de datos y cierra el cursor'''
        self.cursor.close()
        self.bd.close

    def creatTable(self):
        '''Funcion que crea la tabla types.'''
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS types(
                            id_type     INTEGER PRIMARY KEY,
                            description TEXT)''')

    def insertValue(self):
        '''Funcion que inserta los tipos de persona en la tabla types.'''
        self.cursor.execute("INSERT INTO types VALUES(0,'Person')")
        self.cursor.execute("INSERT INTO types VALUES(1,'Group')")
        self.cursor.execute("INSERT INTO types VALUES(2,'Unknown')")

    def creatPerformesTable(self):
        '''Funcion que crea la tabla performers.'''
        self.cursor.execute('''CREATE TABLE performers(
                            id_performer    INTEGER PRIMARY KEY,
                            id_type         INTEGER,
                            name            TEXT,
                            FOREIGN KEY     (id_type) REFERENCES types(id_type))''')

    def creatPersonsTable(self):
        '''Funcion que crea la tabla persons.'''
        self.cursor.execute('''CREATE TABLE persons(
                            id_person   INTEGER PRIMARY KEY,
                            stage_name  TEXT,
                            real_name   TEXT,
                            birth_date  TEXT,
                            death_date  TEXT)''')

    def creatGroupsTable(self):
        '''Funcion que crea la table groups.'''
        self.cursor.execute('''CREATE TABLE groups(
                            id_group    INTEGER PRIMARY KEY,
                            name        TEXT,
                            start_date  TEXT,
                            end_date    TEXT)''')

    def creatAlbumsTable(self):
        '''Funcion que crea la tabla albums.'''
        self.cursor.execute('''CREATE TABLE albums(
                            id_album  INTEGER PRIMARY KEY,
                            path      TEXT,
                            name      TEXT,
                            year      INTEGER)''')

    def creatRolasTable(self):
        '''Funcion que crea la tabla rolas.'''
        self.cursor.execute('''CREATE TABLE rolas(
                            id_rola        INTEGER PRIMARY KEY,
                            id_performer   INTEGER,
                            id_album       INTEGER,
                            path           TEXT,
                            title          TEXT,
                            track          INTEGER,
                            year           INTEGER,
                            genre          TEXT,
                            FOREIGN KEY    (id_performer) REFERENCES performers(id_performer),
                            FOREIGN KEY    (id_album) REFERENCES albums(id_album))''')

    def creatInGroupTable(self):
        '''Funcion que crea la tabla in_group.'''
        self.cursor.execute('''CREATE TABLE in_group(
                            id_person   INTEGER,
                            id_group    INTEGER,
                            PRIMARY KEY (id_person, id_group),
                            FOREIGN KEY (id_person) REFERENCES persons(id_person),
                            FOREIGN KEY (id_group) REFERENCES  groups(id_group))''')



c = DataBase()
