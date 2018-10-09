import sqlite3
import os.path
import os

class Reproductor():

    def __init__(self):
        self.bd = sqlite3.connect("Reproductor.db")
        self.cursor = self.bd.cursor()
        self.creaTables()
        self.bd.commit()
        self.cursor.close()
        self.bd.close

    def creaTables(self):
        self.creaTypesTable()
        self.insertValue()
        self.creatPerformesTable()
        self.creatPersonsTable()
        self.creatGroupsTable()
        self.creatAlbumsTable()
        self.creatRolasTable()
        self.creatInGroupTable()

    def creaTypesTable(self):
        types = "CREATE TABLE IF NOT EXISTS types(id_type INTEGER PRIMARY KEY, description TEXT)"
        self.cursor.execute(types)

    def insertValue(self):
        self.cursor.execute("INSERT INTO types VALUES(0,'Person')")
        self.cursor.execute("INSERT INTO types VALUES(1,'Group')")
        self.cursor.execute("INSERT INTO types VALUES(2,'Unknown')")

    def creatPerformesTable(self):
        performers =  "CREATE TABLE performers ("
        performers += "id_performer INTEGER PRIMARY KEY, "
        performers += "id_type      INTEGER, "
        performers += "name         TEXT, "
        performers += "FOREIGN KEY (id_type) REFERENCES types(id_type))"
        self.cursor.execute(performers)

    def creatPersonsTable(self):
        person  = "CREATE TABLE persons ("
        person += "id_person  INTEGER PRIMARY KEY, "
        person += "stage_name TEXT, "
        person += "real_name  TEXT, "
        person += "birth_date TEXT, "
        person += "death_date TEXT)"

        self.cursor.execute(person)

    def creatGroupsTable(self):
        group  = "CREATE TABLE groups ("
        group += "id_group      INTEGER PRIMARY KEY, "
        group += "name          TEXT, "
        group += "start_date    TEXT, "
        group += "end_date      TEXT)"
        self.cursor.execute(group)

    def creatAlbumsTable(self):
        album  = "CREATE TABLE albums ("
        album += "id_album  INTEGER PRIMARY KEY, "
        album += "path      TEXT, "
        album += "name      TEXT, "
        album += "year      INTEGER)"
        self.cursor.execute(album)

    def creatRolasTable(self):
        rola = "CREATE TABLE rolas ("
        rola += "id_rola        INTEGER PRIMARY KEY, "
        rola += "id_performer   INTEGER, "
        rola += "id_album       INTEGER, "
        rola += "path           TEXT, "
        rola += "title          TEXT, "
        rola += "track          INTEGER, "
        rola += "year           INTEGER, "
        rola += "genre          TEXT, "
        rola += "FOREIGN KEY    (id_performer) REFERENCES performers(id_performer), "
        rola += "FOREIGN KEY    (id_album) REFERENCES albums(id_album))"
        self.cursor.execute(rola)

    def creatInGroupTable(self):
        ingroup  = "CREATE TABLE in_group ("
        ingroup += "id_person   INTEGER, "
        ingroup += "id_group    INTEGER, "
        ingroup += "PRIMARY KEY (id_person, id_group), "
        ingroup += "FOREIGN KEY (id_person) REFERENCES persons(id_person), "
        ingroup += "FOREIGN KEY (id_group) REFERENCES  groups(id_group))"
        self.cursor.execute(ingroup)

c = Reproductor()
