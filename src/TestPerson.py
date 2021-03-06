import unittest
import Person

class TestPerson(unittest.TestCase):
    '''Pruebas unitarias para la clase Person'''
    
    def testSetStageName(self):
        '''Prueba unitaria para setStageName.'''
        self.person1 = Person.Person("Selena Gómez")
        self.person1.setStageName("Selena")
        self.assertEqual("Selena", self.person1.getStageName())

    def testSetRealName(self):
        '''Prueba unitaria para setRealName.'''
        self.person2 = Person.Person("Gareth Emery")
        self.assertEqual("", self.person2.getRealName())
        self.person2.setRealName("Gareth Thomas Rhys Emery")
        self.assertEqual("Gareth Thomas Rhys Emery", self.person2.getRealName())

    def testSetBirthDate(self):
        '''Prueba unitaria para setBirthDate.'''
        self.person3 = Person.Person("Camila Cabello")
        self.assertEqual("", self.person3.getBirthDate())
        self.person3.setBirthDate("3 de marzo de 1997")
        self.assertEqual("3 de marzo de 1997", self.person3.getBirthDate())

    def testSetDeathDate(self):
        '''Pruebas unitarias para setDeathDate.'''
        self.person4 = Person.Person("Michael Jackson")
        self.assertEqual("", self.person4.getDeathDate())
        self.person4.setDeathDate("25 de junio de 2009")
        self.assertEqual("25 de junio de 2009", self.person4.getDeathDate())

    def testGetStageName(self):
        '''Prueba unitaria para getStageName.'''
        self.person10 = Person.Person("Sia")
        self.assertEqual("Sia", self.person10.getStageName())

    def testGetRealName(self):
        '''Prueba unitaria para getRealName.'''
        self.person11 = Person.Person("Katy Perry")
        self.assertEqual("", self.person11.getRealName())
        self.person11.setRealName("Katheryn Elizabeth Hudson")
        self.assertEqual("Katheryn Elizabeth Hudson", self.person11.getRealName())

    def testGetBirthDate(self):
        '''Prueba unitaria para getBirthDate.'''
        self.person12 = Person.Person("Avicii")
        self.assertEqual("", self.person12.getBirthDate())
        self.person12.setBirthDate("20 de abril de 2018")
        self.assertEqual("20 de abril de 2018", self.person12.getBirthDate())

    def testGetDeathDate(self):
        '''Prueba unitaria para getDeathDate.'''
        self.person13 = Person.Person("John Lennon")
        self.assertEqual("", self.person13.getDeathDate())
        self.person13.setDeathDate("8 de diciembre de 1980")
        self.assertEqual("8 de diciembre de 1980", self.person13.getDeathDate())

if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
