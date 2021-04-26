import unittest
from userStory16 import userStory16


class TestUserStory16Class(unittest.TestCase):
    def testUserStory16_1(self):
        resultsList = userStory16("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory16_2(self):
        resultsList = userStory16("AkhileshReddyFamily_US16_01.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: FAMILY: US16: Child I1\'s last name (Mram) does not match family name (Reddy) in family F1.'])


if __name__ == '__main__':
    unittest.main()
