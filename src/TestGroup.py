import unittest
import Group

class TestGroup(unittest.TestCase):
    '''Pruebas unitarias para la clase Group'''
    
    def testGetName(self):
        '''Prueba unitaria para getName.'''
        self.group2 = Group.Group("Maroon 5")
        self.assertEqual("Maroon 5", self.group2.getName())

    def testGetStarDate(self):
        '''Prueba unitaria para getStarDate.'''
        self.group3 = Group.Group("Coldplay")
        self.assertEqual("", self.group3.getStarDate())
        self.group3.setStarDate("1996")
        self.assertEqual("1996", self.group3.getStarDate())

    def testGetEndDate(self):
        '''Prueba unitaria para getEndDate.'''
        self.group4 = Group.Group("Pink Floyd")
        self.assertEqual("", self.group4.getEndDate())
        self.group4.setEndDate("1995")
        self.assertEqual("1995", self.group4.getEndDate())

    def testSetName(self):
        '''Prueba unitaria para setName.'''
        self.group8 = Group.Group("Maroon 5")
        self.assertEqual("Maroon 5", self.group8.getName())

    def testSetStarDate(self):
        '''Prueba unitaria para setStartDate.'''
        self.group9 = Group.Group("Coldplay")
        self.assertEqual("", self.group9.getStarDate())
        self.group9.setStarDate("1996")
        self.assertEqual("1996", self.group9.getStarDate())

    def testSetEndDate(self):
        '''Prueba unitaria para setEndDate.'''
        self.group10 = Group.Group("Pink Floyd")
        self.assertEqual("", self.group10.getEndDate())
        self.group10.setEndDate("1995")
        self.assertEqual("1995", self.group10.getEndDate())

if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
