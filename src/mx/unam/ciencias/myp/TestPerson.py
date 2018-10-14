import unittest
import Person

class TestPerson(unittest.TestCase):

    def testSetStageName(self):
        self.person1 = Person.Person("Selena Gómez")
        self.person1.setStageName("Selena")
        self.assertEqual("Selena", self.person1.getStageName())

    def testSetRealName(self):
        self.person2 = Person.Person("Gareth Emery")
        self.assertEqual("", self.person2.getRealName())
        self.person2.setRealName("Gareth Thomas Rhys Emery")
        self.assertEqual("Gareth Thomas Rhys Emery", self.person2.getRealName())

    def testSetBirthDate(self):
        self.person3 = Person.Person("Camila Cabello")
        self.assertEqual("", self.person3.getBirthDate())
        self.person3.setBirthDate("3 de marzo de 1997")
        self.assertEqual("3 de marzo de 1997", self.person3.getBirthDate())

    def testSetDeathDate(self):
        self.person4 = Person.Person("Michael Jackson")
        self.assertEqual("", self.person4.getDeathDate())
        self.person4.setDeathDate("25 de junio de 2009")
        self.assertEqual("25 de junio de 2009", self.person4.getDeathDate())

    def testAddOcuppation(self):
        self.person5 = Person.Person("Martin Garrix")
        self.assertEqual("", self.person5.getOccupation())
        self.person5.addOcuppation("DJ")
        self.assertEqual("DJ", self.person5.getOccupation())

    def testAddSongs(self):
        self.person7 = Person.Person("Ellie Goulding")
        self.assertEqual([], self.person7.getSongs())
        self.person7.addSongs("Love Me Like You Do")
        self.assertEqual(["Love Me Like You Do"], self.person7.getSongs())

    def testAddAlbums(self):
        self.person8 = Person.Person("Julieta Venegas")
        self.assertEqual([], self.person8.getAlbums())
        self.person8.addAlbums("Limón y Sal")
        self.assertEqual(["Limón y Sal"], self.person8.getAlbums())

    def testGetStageName(self):
        self.person10 = Person.Person("Sia")
        self.assertEqual("Sia", self.person10.getStageName())

    def testGetRealName(self):
        self.person11 = Person.Person("Katy Perry")
        self.assertEqual("", self.person11.getRealName())
        self.person11.setRealName("Katheryn Elizabeth Hudson")
        self.assertEqual("Katheryn Elizabeth Hudson", self.person11.getRealName())

    def testGetBirthDate(self):
        self.person12 = Person.Person("Avicii")
        self.assertEqual("", self.person12.getBirthDate())
        self.person12.setBirthDate("20 de abril de 2018")
        self.assertEqual("20 de abril de 2018", self.person12.getBirthDate())

    def testGetDeathDate(self):
        self.person13 = Person.Person("John Lennon")
        self.assertEqual("", self.person13.getDeathDate())
        self.person13.setDeathDate("8 de diciembre de 1980")
        self.assertEqual("8 de diciembre de 1980", self.person13.getDeathDate())

    def testGetOccupation(self):
        self.person14 = Person.Person("Lady Gaga")
        self.assertEqual("", self.person14.getOccupation())
        self.person14.addOcuppation("Interprete")
        self.assertEqual("Interprete", self.person14.getOccupation())

    def testGetSongs(self):
        self.person16 = Person.Person("Alan Walker")
        self.assertEqual([], self.person16.getSongs())
        self.person16.addSongs("Animals")
        self.assertEqual(["Animals"], self.person16.getSongs())

    def testGetAlbums(self):
        self.person17 = Person.Person("Belanova")
        self.assertEqual([], self.person17.getAlbums())
        self.person17.addAlbums("Viaje al centro del corazón")
        self.assertEqual(["Viaje al centro del corazón"], self.person17.getAlbums())

    def testGetGenre(self):
        self.person19 = Person.Person("Steve Aoki")
        self.assertEqual("", self.person19.getGenre())
        self.person19.setGenre("Electronic")
        self.assertEqual("Electronic", self.person19.getGenre())

    def testSetGenre(self):
        self.person20 = Person.Person("Steve Aoki")
        self.assertEqual("", self.person20.getGenre())
        self.person20.setGenre("Electronic")
        self.assertEqual("Electronic", self.person20.getGenre())

if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
