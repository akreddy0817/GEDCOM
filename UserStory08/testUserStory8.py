import unittest
from userStory8 import userStory08

class TestUserStory08Class(unittest.TestCase):
    def testUserStory08_1(self):
        results = userStory08("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(results, [])
    
    def testUserStory08_2(self):
        results = userStory08("AkhileshReddyFamily_US08_01.ged")
        self.maxDiff = None
        self.assertEqual(results, [
            "ERROR: FAMILY: US08: Child's birthday occurs more than 9 months after parents' divorce. ID: F6 Child's birthday: 2015-10-10 Parents' divorce date: 2010-01-09"
        ])

    def testUserStory08_3(self):
        results = userStory08("AkhileshReddyFamily_US08_02.ged")
        self.maxDiff = None
        self.assertEqual(results, [
            "ERROR: FAMILY: US08: Child's birthday occurs before parents' marriage. ID: F3 Child's birthday: 1952-08-02 Parents' marriage date: 1960-08-06",
            "ERROR: FAMILY: US08: Child's birthday occurs before parents' marriage. ID: F3 Child's birthday: 1901-09-09 Parents' marriage date: 1960-08-06",
            "ERROR: FAMILY: US08: Child's birthday occurs more than 9 months after parents' divorce. ID: F6 Child's birthday: 2015-10-10 Parents' divorce date: 2010-01-09"
        ])


if __name__ == '__main__':
    unittest.main()