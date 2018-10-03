import unittest
import Albums

class TestPerson(unittest.TestCase):

    def testGetIdentifier(self):
        self.album1 = Albums.Albums("The Fame", "/Users/teresabecerril/Music")
        self.assertEqual("The Fame", self.album1.getIdentifier())

    def testGetPath(self):
        self.album2 = Albums.Albums("Witness", "/Users/teresabecerril/Music")
        self.assertEqual("/Users/teresabecerril/Music", self.album2.getPath())

    def testGetName(self):
        self.album3 = Albums.Albums("One of the Boys", "/Users/teresabecerril/Music")
        self.assertEqual("", self.album3.getName())
        self.album3.setName("Teenage Dream")
        self.assertEqual("Teenage Dream", self.album3.getName())

    def testGetYear(self):
        self.album4 = Albums.Albums("The Fame", "/Users/teresabecerril/Music")
        self.assertEqual(0, self.album4.getYear())
        self.album4.setYear(2017)
        self.assertEqual(2017, self.album4.getYear())

    def testSetName(self):
        self.album5 = Albums.Albums("One of the Boys", "/Users/teresabecerril/Music")
        self.assertEqual("", self.album5.getName())
        self.album5.setName("Teenage Dream")
        self.assertEqual("Teenage Dream", self.album5.getName())

    def testSetYear(self):
        self.album6 = Albums.Albums("The Fame", "/Users/teresabecerril/Music")
        self.assertEqual(0, self.album6.getYear())
        self.album6.setYear(2017)
        self.assertEqual(2017, self.album6.getYear())

if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
