import unittest
from userStory5 import userStory05



class TestUserStory05Class(unittest.TestCase):

    def testUserStory05_1(self):
        results = userStory05("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(results, [])
    
    def testUserStory05_2(self):
        results = userStory05("AkhileshReddyFamily_US5_01.ged")
        self.maxDiff = None
        self.assertEqual(results,['ERROR: FAMILY: US05: The wedding occurs after husband death. Wedding Date: 2018-08-06 Husband Death: 2017-10-11'])

    def testUserStory05_3(self):
        results = userStory05("AkhileshReddyFamily_US5_02.ged")
        self.maxDiff = None
        self.assertEqual(results,['ERROR: FAMILY: US05: The wedding occurs after wife death. Wedding Date: 2020-08-06 Wife Death: 2019-02-14', 'ERROR: FAMILY: US05: The wedding occurs after husband death. Wedding Date: 2020-08-06 Husband Death: 2017-10-11'])
if __name__ == '__main__':
    unittest.main()