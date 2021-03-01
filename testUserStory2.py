import unittest
from userStory2 import userStory02


#User story 02: Birth should occur before marriage of an individual


class TestUserStory02Class(unittest.TestCase):

    def testUserStory02_1(self):
        resultsList = userStory02("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])
    def testUserStory02_2(self):
        resultsList = userStory02("AkhileshReddyFamily_US2_02.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ERROR: FAMILY: US02: : I3: Wife's birth date 2020-08-02 is after marriage date 1995-03-05"])
    def testUserStory02_3(self):
        resultsList = userStory02("AkhileshReddyFamily_US2_03.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,["ERROR: FAMILY: US02: : I3: Wife's birth date 2020-08-02 is after marriage date 1995-03-05", "ERROR: FAMILY: US02: : I7: Husband's birth date 2020-08-29 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: : I8: Wife's birth date 2020-11-20 is after marriage date 1960-08-06"])
    def testUserStory02_4(self):
        resultsList = userStory02("AkhileshReddyFamily_US2_04.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,["ERROR: FAMILY: US02: : I3: Wife's birth date 2020-08-02 is after marriage date 1995-03-05", "ERROR: FAMILY: US02: : I7: Husband's birth date 2020-08-29 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: : I8: Wife's birth date 2020-11-20 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: : I13: Wife's birth date 2020-10-10 is after marriage date 2003-09-08"])
    def testUserStory02_5(self):
        resultsList = userStory02("AkhileshReddyFamily_US2_05.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,["ERROR: FAMILY: US02: : I3: Wife's birth date 2020-08-02 is after marriage date 1995-03-05", "ERROR: FAMILY: US02: : I7: Husband's birth date 2020-08-29 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: : I8: Wife's birth date 2020-11-20 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: : I12: Husband's birth date 2021-09-09 is after marriage date 2003-09-08"] )
if __name__ == '__main__':
    unittest.main()