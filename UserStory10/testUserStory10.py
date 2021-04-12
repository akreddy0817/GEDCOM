import unittest
from userStory10 import userStory10


class TestUserStory10Class(unittest.TestCase):

    def testUserStory10_1(self):
        resultsList = userStory10("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory10_2(self):
        resultsList = userStory10("AkhileshReddyFamily_US10_01.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: FAMILY: US10: F2: Husband (I5) birth date 1950-10-07 not at least 14 years prior to marriage date 1955-02-01', 'ERROR: FAMILY: US10: F2: Wife (I6) birth date 1941-09-13 not at least 14 years prior to marriage date 1955-02-01'])
    


if __name__ == '__main__':
    unittest.main()