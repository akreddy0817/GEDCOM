import unittest
from userStory21 import userStory21


class TestUserStory21Class(unittest.TestCase):

    def testUserStory21_1(self):
        resultsList = userStory21("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory21_2(self):
        resultsList = userStory21("AkhileshReddyFamily_US12_01.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: FAMILY: US21: F1: Wife (I3) is labelled incorrectly as (M).'])

    def testUserStory21_3(self):
        resultsList = userStory21("AkhileshReddyFamily_US12_02.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: FAMILY: US21: F1: Wife (I3) is labelled incorrectly as (M).', 'ERROR: FAMILY: US21: F2: Husband (I5) is labelled incorrectly as (F).'])
if __name__ == '__main__':
    unittest.main()