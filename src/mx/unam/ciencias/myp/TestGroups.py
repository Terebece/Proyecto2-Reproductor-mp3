import unittest
import Groups

class TestPerson(unittest.TestCase):

    def testGetName(self):
        self.group2 = Groups.Groups("Maroon 5")
        self.assertEqual("Maroon 5", self.group2.getName())

    def testGetStarDate(self):
        self.group3 = Groups.Groups("Coldplay")
        self.assertEqual("", self.group3.getStarDate())
        self.group3.setStarDate("1996")
        self.assertEqual("1996", self.group3.getStarDate())

    def testGetEndDate(self):
        self.group4 = Groups.Groups("Pink Floyd")
        self.assertEqual("", self.group4.getEndDate())
        self.group4.setEndDate("1995")
        self.assertEqual("1995", self.group4.getEndDate())

    def testGetIntegrants(self):
        self.group5 = Groups.Groups("Coldplay")
        self.assertEqual("", self.group5.getIntegrants())
        self.group5.addIntegrant("Chris Martin")
        self.group5.addIntegrant("Guy Berryman")
        self.assertEqual("Chris Martin, Guy Berryman", self.group5.getIntegrants())

    def testGetSongs(self):
        self.group6 = Groups.Groups("Maroon 5")
        self.assertEqual([], self.group6.getSongs())
        self.group6.addSong("Sugar")
        self.group6.addSong("What Lovers Do")
        self.assertEqual(["Sugar", "What Lovers Do"], self.group6.getSongs())

    def testGetGenre(self):
        self.group7 = Groups.Groups("Pink Floyd")
        self.assertEqual("", self.group7.getGenre())
        self.group7.setGenre("Rock progresivo")
        self.assertEqual("Rock progresivo", self.group7.getGenre())

    def testSetName(self):
        self.group8 = Groups.Groups("Maroon 5")
        self.assertEqual("Maroon 5", self.group8.getName())

    def testSetStarDate(self):
        self.group9 = Groups.Groups("Coldplay")
        self.assertEqual("", self.group9.getStarDate())
        self.group9.setStarDate("1996")
        self.assertEqual("1996", self.group9.getStarDate())

    def testSetEndDate(self):
        self.group10 = Groups.Groups("Pink Floyd")
        self.assertEqual("", self.group10.getEndDate())
        self.group10.setEndDate("1995")
        self.assertEqual("1995", self.group10.getEndDate())

    def testSetIntegrants(self):
        self.group11 = Groups.Groups("Coldplay")
        self.assertEqual("", self.group11.getIntegrants())
        self.group11.addIntegrant("Chris Martin")
        self.group11.addIntegrant("Guy Berryman")
        self.assertEqual("Chris Martin, Guy Berryman", self.group11.getIntegrants())

    def testSetSongs(self):
        self.group12 = Groups.Groups("Maroon 5")
        self.assertEqual([], self.group12.getSongs())
        self.group12.addSong("Sugar")
        self.group12.addSong("What Lovers Do")
        self.assertEqual(["Sugar", "What Lovers Do"], self.group12.getSongs())

    def testSetGenre(self):
        self.group13 = Groups.Groups("Pink Floyd")
        self.assertEqual("", self.group13.getGenre())
        self.group13.setGenre("Rock progresivo")
        self.assertEqual("Rock progresivo", self.group13.getGenre())

if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
