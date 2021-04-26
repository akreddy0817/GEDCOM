import unittest
from userStory15 import userStory15


class TestUserStory15Class(unittest.TestCase):
    def testUserStory15_1(self):
        resultsList = userStory15("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory15_2(self):
        resultsList = userStory15("AkhileshReddyFamily_US15_01.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: FAMILY: US15: Family F5 has 16 siblings.'])


if __name__ == '__main__':
    unittest.main()
