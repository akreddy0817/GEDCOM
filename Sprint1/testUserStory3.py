import unittest
from userStory3 import userStory03


#User story 03: Birth should occur before death of an individual


class TestUserStory03Class(unittest.TestCase):
    def testUserStory03_1(self):
        resultsList = userStory03("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory03_2(self):
        resultsList = userStory03("AkhileshReddyFamily_US3_02.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [
            "ERROR: INDIVIDUAL: US03: : I5: Person's birth date 2020-10-07 is after death date 1999-04-13"
        ])

    def testUserStory03_3(self):
        resultsList = userStory03("AkhileshReddyFamily_US3_03.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [
            "ERROR: INDIVIDUAL: US03: : I5: Person's birth date 2020-10-07 is after death date 1999-04-13",
            "ERROR: INDIVIDUAL: US03: : I7: Person's birth date 2020-08-29 is after death date 2017-10-11",
            "ERROR: INDIVIDUAL: US03: : I8: Person's birth date 2020-11-20 is after death date 2019-02-14"
        ])

    def testUserStory03_4(self):
        resultsList = userStory03("AkhileshReddyFamily_US3_04.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [
            "ERROR: INDIVIDUAL: US03: : I6: Person's birth date 2020-09-13 is after death date 2001-11-12",
            "ERROR: INDIVIDUAL: US03: : I7: Person's birth date 2020-08-29 is after death date 2017-10-11",
            "ERROR: INDIVIDUAL: US03: : I8: Person's birth date 2020-11-20 is after death date 2019-02-14"
        ])

    def testUserStory03_5(self):
        resultsList = userStory03("AkhileshReddyFamily_US3_05.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [
            "ERROR: INDIVIDUAL: US03: : I5: Person's birth date 2020-10-07 is after death date 1999-04-13",
            "ERROR: INDIVIDUAL: US03: : I6: Person's birth date 2020-09-13 is after death date 2001-11-12",
            "ERROR: INDIVIDUAL: US03: : I7: Person's birth date 2020-08-29 is after death date 2017-10-11",
            "ERROR: INDIVIDUAL: US03: : I8: Person's birth date 2020-11-20 is after death date 2019-02-14",
        ])


if __name__ == '__main__':
    unittest.main()