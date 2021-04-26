import unittest
from userStory23 import userStory23


class TestUserStory23Class(unittest.TestCase):

    def testUserStory23_1(self):
        resultsList = userStory23("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory23_2(self):
        resultsList = userStory23("AkhileshReddyFamily_US23_01.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US23: Two individuals have duplicate names and birthdays [Akhilesh Reddy, 2000-08-17].'])

if __name__ == '__main__':
    unittest.main()