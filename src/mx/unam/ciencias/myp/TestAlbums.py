import unittest
import Albums

class TestPerson(unittest.TestCase):

    def testGetPath(self):
        self.album2 = Albums.Albums("/Users/teresabecerril/Music", "Witness")
        self.assertEqual("/Users/teresabecerril/Music", self.album2.getPath())

    def testGetName(self):
        self.album3 = Albums.Albums("/Users/teresabecerril/Music", "One of the Boys")
        self.assertEqual("One of the Boys", self.album3.getName())
        self.album3.setName("Teenage Dream")
        self.assertEqual("Teenage Dream", self.album3.getName())

    def testGetYear(self):
        self.album4 = Albums.Albums("/Users/teresabecerril/Music", "The Fame")
        self.assertEqual(0, self.album4.getYear())
        self.album4.setYear(2017)
        self.assertEqual(2017, self.album4.getYear())

    def testGetGenre(self):
        self.album5 = Albums.Albums("/Users/teresabecerril/Music", "Neon Future")
        self.assertEqual("", self.album5.getGenre())
        self.album5.setGenre("Electronic")
        self.assertEqual("Electronic", self.album5.getGenre())

    def testGetArtist(self):
        self.album6 = Albums.Albums("/Users/teresabecerril/Music", "A Head Full of Dreams")
        self.assertEqual("", self.album6.getArtist())
        self.album6.setArtist("Coldplay")
        self.assertEqual("Coldplay", self.album6.getArtist())

    def testGetSongs(self):
        self.album7 = Albums.Albums("/Users/teresabecerril/Music", "Witness")
        self.assertEqual("", self.album7.getSongs())
        self.album7.addSong("Chained to the Rhythm")
        self.assertEqual("Chained to the Rhythm", self.album7.getSongs())

    def testSetName(self):
        self.album8 = Albums.Albums("/Users/teresabecerril/Music", "One of the Boys")
        self.assertEqual("One of the Boys", self.album8.getName())
        self.album8.setName("Teenage Dream")
        self.assertEqual("Teenage Dream", self.album8.getName())

    def testSetYear(self):
        self.album7 = Albums.Albums("/Users/teresabecerril/Music", "The Fame")
        self.assertEqual(0, self.album7.getYear())
        self.album7.setYear(2017)
        self.assertEqual(2017, self.album7.getYear())

    def testSetGenre(self):
        self.album8 = Albums.Albums("/Users/teresabecerril/Music", "Neon Future")
        self.assertEqual("", self.album8.getGenre())
        self.album8.setGenre("Electronic")
        self.assertEqual("Electronic", self.album8.getGenre())

    def testSetArtist(self):
        self.album9 = Albums.Albums("/Users/teresabecerril/Music", "A Head Full of Dreams")
        self.assertEqual("", self.album9.getArtist())
        self.album9.setArtist("Coldplay")
        self.assertEqual("Coldplay", self.album9.getArtist())

    def testSetSongs(self):
        self.album10 = Albums.Albums("/Users/teresabecerril/Music", "Witness")
        self.assertEqual("", self.album10.getSongs())
        self.album10.addSong("Chained to the Rhythm")
        self.assertEqual("Chained to the Rhythm", self.album10.getSongs())

if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
