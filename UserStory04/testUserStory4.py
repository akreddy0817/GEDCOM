import unittest
from userStory4 import userStory04


#User story 04: Marriage before divorce




class TestUserStory04Class(unittest.TestCase):

    def testUserStory04_1(self):
        results = userStory04("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(results, [])
    
    def testUserStory04_2(self):
        results = userStory04("AkhileshReddyFamily_US4_01.ged")
        self.maxDiff = None
        self.assertEqual(results,['ERROR: FAMILY: US04:F6 Divorce date occurs before marriage date - Marriage 2020-09-08: Divorce 2010-01-09'] )
    
if __name__ == '__main__':
    unittest.main()