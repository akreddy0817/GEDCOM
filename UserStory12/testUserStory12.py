import unittest
from userStory12 import userStory12


class TestUserStory12Class(unittest.TestCase):

    def testUserStory12_1(self):
        resultsList = userStory12("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory12_2(self):
        resultsList = userStory12("AkhileshReddyFamily_US12_01.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US12: I5: Father I5 is more than 80 years older than his child (I2): Raj Reddy.', 'ERROR: INDIVIDUAL: US12: I5: Father I5 is more than 80 years older than his child (I9): Dhruv Reddy.'])


if __name__ == '__main__':
    unittest.main()