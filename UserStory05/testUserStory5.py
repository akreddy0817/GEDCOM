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
        self.assertEqual(results,['ERROR: FAMILY: US05: Wedding 2018-08-06 occurs after Husband death 2017-10-11.'])

    def testUserStory05_3(self):
        results = userStory05("AkhileshReddyFamily_US5_02.ged")
        self.maxDiff = None
        self.assertEqual(results,['ERROR: FAMILY: US05: Wedding 2020-08-06 occurs after Wife death 2019-02-14.', 'ERROR: FAMILY: US05: Wedding 2020-08-06 occurs after Husband death 2017-10-11.'])
if __name__ == '__main__':
    unittest.main()