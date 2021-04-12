import unittest
from userStory9 import userStory09

'''
User story 09: Birth before death of parents
'''


class TestUserStory09Class(unittest.TestCase):

    def testUserStory09_1(self):
        resultsList = userStory09("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory09_2(self):
        resultsList = userStory09("AkhileshReddyFamily_US9_01.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ERROR: FAMILY: US09: F2: Husband (I5) died 1956-04-13 before child's (I2) birth 1961-05-19", "ERROR: FAMILY: US09: F2: Husband (I5) died 1956-04-13 before child's (I9) birth 1967-10-11"])
    
    def testUserStory09_3(self):
        resultsList = userStory09("AkhileshReddyFamily_US9_02.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ERROR: FAMILY: US09: F2: Husband (I5) died 1956-04-13 before child's (I2) birth 1961-05-19", "ERROR: FAMILY: US09: F2: Wife (I6) died 1956-11-12 before child's (I2) birth 1961-05-19", "ERROR: FAMILY: US09: F2: Husband (I5) died 1956-04-13 before child's (I9) birth 1967-10-11", "ERROR: FAMILY: US09: F2: Wife (I6) died 1956-11-12 before child's (I9) birth 1967-10-11"])



if __name__ == '__main__':
    unittest.main()