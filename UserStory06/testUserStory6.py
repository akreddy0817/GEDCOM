import unittest
from userStory6 import userStory06



class TestUserStory06Class(unittest.TestCase):

    def testUserStory06_1(self):
        results = userStory06("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(results, [])
    
    def testUserStory06_2(self):
        results = userStory06("AkhileshReddyFamily_US6_01.ged")
        self.maxDiff = None
        self.assertEqual(results,['ERROR: FAMILY: US06: divorce occurs after husband death. Divorce Date: 2018-01-09 Husband Death: 2017-10-11'])
    def testUserStory06_3(self):
        results = userStory06("AkhileshReddyFamily_US6_02.ged")
        self.maxDiff = None
        self.assertEqual(results,['ERROR: FAMILY: US06: divorce occurs after wife death. Divorce Date: 2020-01-09 Wife Death: 2019-02-14', 'ERROR: FAMILY: US06: divorce occurs after husband death. Divorce Date: 2020-01-09 Husband Death: 2017-10-11'])


if __name__ == '__main__':
    unittest.main()