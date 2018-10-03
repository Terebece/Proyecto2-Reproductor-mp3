import unittest
import Groups

class TestPerson(unittest.TestCase):

    def testGetIdentifier(self):
        self.group1 = Groups.Groups("The Beatles")
        self.assertEqual("The Beatles", self.group1.getIdentifier())

    def testGetName(self):
        self.group2 = Groups.Groups("Maroon 5")
        self.assertEqual("", self.group2.getName())
        self.group2.setName("Maroon")
        self.assertEqual("Maroon", self.group2.getName())

    def testGetStarDate(self):
        self.group3 = Groups.Groups("Coldplay")
        self.assertEqual("", self.group3.getStarDate())
        self.group3.setStarDate("1996")
        self.assertEqual("1996", self.group3.getStarDate())

    def testGetEndDate(self):
        self.group4 = Groups.Groups("Pink Floy")
        self.assertEqual("", self.group4.getEndDate())
        self.group4.setEndDate("1995")
        self.assertEqual("1995", self.group4.getEndDate())


    def testSetName(self):
        self.group5 = Groups.Groups("Maroon 5")
        self.assertEqual("", self.group5.getName())
        self.group5.setName("Maroon")
        self.assertEqual("Maroon", self.group5.getName())

    def testSetStarDate(self):
        self.group6 = Groups.Groups("Coldplay")
        self.assertEqual("", self.group6.getStarDate())
        self.group6.setStarDate("1996")
        self.assertEqual("1996", self.group6.getStarDate())

    def testSetEndDate(self):
        self.group7 = Groups.Groups("Pink Floy")
        self.assertEqual("", self.group7.getEndDate())
        self.group7.setEndDate("1995")
        self.assertEqual("1995", self.group7.getEndDate())

if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
