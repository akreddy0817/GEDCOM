import unittest
from userStory24 import userStory24


class TestUserStory24Class(unittest.TestCase):

    def testUserStory24_1(self):
        resultsList = userStory24("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory24_2(self):
        resultsList = userStory24("AkhileshReddyFamily_US24_01.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: FAMILY: US24: Two families [F1, F5] have duplicate spouses [Raj Reddy, Sapna Aruva].'])

if __name__ == '__main__':
    unittest.main()