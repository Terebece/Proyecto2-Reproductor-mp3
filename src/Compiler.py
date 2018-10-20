class Compiler:

    def __init__(self):
        self.long = 0

    def readString(self, consulta):
        '''Funcion que lee la cadena de la consulta,
           puede buscar por Al: = Album, A: = Artista, 
           T: = Titulo, G: = Genero y Y: = año'''
        self.long = len(consulta)
        '''Las consultas deben de terminar con :. '''
        if consulta.find(":.", self.long-2, self.long) != -1:
            cons = consulta.strip(":.")
            if cons.find("Al:", 0, 4) != -1:
                return self.readAlbum(cons)

            elif cons.find("A:", 0, 3) != -1:
                return self.readArtist(cons)

            elif cons.find("T:", 0, 3) != -1:
                return self.readTitle(cons)

            elif cons.find("G:", 0, 3) != -1:
                return self.readGenre(cons)

            elif cons.find("Y:", 0, 3) != -1:
                return self.readYear(cons)

            else:
                return "Consulta invalida"

    def readAlbum(self, cons):
        '''Funcion que hace una consulta por albums.'''
        if cons.find(";") == -1:
            cons = cons.strip("Al: ")
            Dao.getAlbum(cons)
        else:
            if cons.find(";;") != -1:
                self.twoConsults(cons, ";;")
            elif cons.find(";:") != -1:
                self.twoConsults(cons, ";:")

    def readArtist(self, cons):
        '''Funcion que hace una consulta por artista.'''
        if cons.find(";") == -1:
            cons = cons.strip("A: ")
            Dao.getArtist(cons)
        else:
            if cons.find(";;") != -1:
                self.twoConsults(cons, ";;")
            elif cons.find(";:") != -1:
                self.twoConsults(cons, ";:")


    def readTitle(self, cons):
        '''Funcion que hace una consulta por titulo.''' 
        if cons.find(";") == -1:
            cons = cons.strip("T: ")
            Dao.getTitle(cons)
        else:
            if cons.find(";;") != -1:
                self.twoConsults(cons, ";;")
            elif cons.find(";:") != -1:
                self.twoConsults(cons, ";:")

    def readGenre(self, cons):
        '''Funcion que hace una consulta por genero.'''
        if cons.find(";") == -1:
            cons = cons.strip("G: ")
            Dao.getGenre()
        else:
            if cons.find(";;") != -1:
                self.twoConsults(cons, ";;")
            elif cons.find(";:") != -1:
                self.twoConsults(cons, ";:")

    def readYear(cons):
        '''Funcion que hace una consulta por año.'''
        if cons.find("-") == -1:
            Dao.getYear(cons)
        else:
            listr = []
            d = years.split("-")
            i = int(d[0])
            while i <= int(d[1]):
                listr.append(i)
                i += 1
            for d in listr:
                Dao.getYear(d)

    def twoConsults(self, consulta, op):
        '''Funcion que hace dos consultas'''
        cons = consulta.split(op)
        cons1 = self.types(cons[0])
        cons2 = self.types(cons[1])
        consultasT = []
        '''    ;;  =  y  '''    
        if op == ";;":
            if cons1 != [] and cons2 != []:
                consultasT = cons1 + cons2
        '''    ;:  = o   '''
        elif op == ";:":
            if cons1 != [] or cons2 != []:
                consultasT = cons1 + cons2

    def types(self, cons):
        '''Regresa la consulta dependiende del tipo'''
        if cons.find("Al:", 0, 4) != -1:
            con = cons.strip("Al: ")
            Dao.getAlbum(con)
        elif cons.find("A:", 0, 3) != -1:
            cons = cons.strip("A: ")
            Dao.getArtist(con)
        elif cons.find("T:", 0, 3) != -1:
            cons = cons.strip("T: ")
            Dao.getTitle(con)
        elif cons.find("G:", 0, 3) != -1:
            cons = cons.strip("G: ")
            Dao.getGenre(con)
        return c
