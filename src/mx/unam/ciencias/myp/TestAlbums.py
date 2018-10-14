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

    def testGetPerformer(self):
        self.album6 = Albums.Albums("/Users/teresabecerril/Music", "A Head Full of Dreams")
        self.assertEqual("", self.album6.getPerformer())
        self.album6.setPerformer("Coldplay")
        self.assertEqual("Coldplay", self.album6.getPerformer())

    def testGetSongs(self):
        self.album7 = Albums.Albums("/Users/teresabecerril/Music", "Witness")
        self.assertEqual([], self.album7.getSongs())
        self.album7.addSong("Chained to the Rhythm")
        self.album7.addSong("E.T.")
        self.assertEqual(["Chained to the Rhythm", "E.T."], self.album7.getSongs())

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

    def testSetPerformer(self):
        self.album9 = Albums.Albums("/Users/teresabecerril/Music", "A Head Full of Dreams")
        self.assertEqual("", self.album9.getPerformer())
        self.album9.setPerformer("Coldplay")
        self.assertEqual("Coldplay", self.album9.getPerformer())

    def testSetSongs(self):
        self.album10 = Albums.Albums("/Users/teresabecerril/Music", "Witness")
        self.assertEqual([], self.album10.getSongs())
        self.album10.addSong("Chained to the Rhythm")
        self.album10.addSong("E.T.")
        self.assertEqual(["Chained to the Rhythm", "E.T."], self.album10.getSongs())

if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
