import unittest
from userStory1_2 import userStory01

from userStory1_2 import userStory02



#User story 01: Dates before current date



class TestUserStory01Class(unittest.TestCase):
    
    def testUserStory01_1(self):
        results = userStory01("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(results, [])
        
    def testUserStory01_2(self):
        results = userStory01("AkhileshReddyFamily_US1_01.ged")
        self.maxDiff = None
        self.assertEqual(results, ['ERROR: INDIVIDUAL: US01: I2: Marriage 2100-03-05 occurs in the future', 'ERROR: INDIVIDUAL: US01: I3: Marriage 2100-03-05 occurs in the future'])
    
    def testUserStory01_3(self):
        results= userStory01("AkhileshReddyFamily_US1_02.ged")
        self.maxDiff = None
        self.assertEqual(results,['ERROR: INDIVIDUAL: US01: I2: Marriage 2100-03-05 occurs in the future', 'ERROR: INDIVIDUAL: US01: I3: Marriage 2100-03-05 occurs in the future', 'ERROR: INDIVIDUAL: US01: I12: Divorce 2100-01-09 occurs in the future', 'ERROR: INDIVIDUAL: US01: I13: Divorce 2100-01-09 occurs in the future'])
    
    def testUserStory01_4(self):
        results = userStory01("AkhileshReddyFamily_US1_03.ged")
        self.maxDiff = None
        self.assertEqual(results,['ERROR: INDIVIDUAL: US01: I2: Marriage 2100-03-05 occurs in the future', 'ERROR: INDIVIDUAL: US01: I2: Birthday 2200-05-19 occurs in the future', 'ERROR: INDIVIDUAL: US01: I3: Marriage 2100-03-05 occurs in the future', 'ERROR: INDIVIDUAL: US01: I12: Divorce 2100-01-09 occurs in the future', 'ERROR: INDIVIDUAL: US01: I13: Divorce 2100-01-09 occurs in the future'])
    
    def testUserStory01_5(self):
        results = userStory01("AkhileshReddyFamily_US1_04.ged")
        self.maxDiff = None
        self.assertEqual(results,['ERROR: INDIVIDUAL: US01: I2: Marriage 2100-03-05 occurs in the future', 'ERROR: INDIVIDUAL: US01: I2: Birthday 2200-05-19 occurs in the future', 'ERROR: INDIVIDUAL: US01: I3: Marriage 2100-03-05 occurs in the future', 'ERROR: INDIVIDUAL: US01: I3: Birthday 2260-08-02 occurs in the future', 'ERROR: INDIVIDUAL: US01: I12: Divorce 2100-01-09 occurs in the future', 'ERROR: INDIVIDUAL: US01: I13: Divorce 2100-01-09 occurs in the future'])
    
    def testUserStory02_1(self):
        resultsList = userStory02("AkhileshReddyFamily.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def testUserStory02_2(self):
        resultsList = userStory02("AkhileshReddyFamily_US2_02.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ERROR: FAMILY: US02: I3: Wife's birth date 2020-08-02 is after marriage date 1995-03-05"])
    def testUserStory02_3(self):
        resultsList = userStory02("AkhileshReddyFamily_US2_03.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,["ERROR: FAMILY: US02: I3: Wife's birth date 2020-08-02 is after marriage date 1995-03-05", "ERROR: FAMILY: US02: I7: Husband's birth date 2020-08-29 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: I8: Wife's birth date 2020-11-20 is after marriage date 1960-08-06"])
    def testUserStory02_4(self):
        resultsList = userStory02("AkhileshReddyFamily_US2_04.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,["ERROR: FAMILY: US02: I3: Wife's birth date 2020-08-02 is after marriage date 1995-03-05", "ERROR: FAMILY: US02: I7: Husband's birth date 2020-08-29 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: I8: Wife's birth date 2020-11-20 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: I13: Wife's birth date 2020-10-10 is after marriage date 2003-09-08"])
    def testUserStory02_5(self):
        resultsList = userStory02("AkhileshReddyFamily_US2_05.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,["ERROR: FAMILY: US02: I3: Wife's birth date 2020-08-02 is after marriage date 1995-03-05", "ERROR: FAMILY: US02: I7: Husband's birth date 2020-08-29 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: I8: Wife's birth date 2020-11-20 is after marriage date 1960-08-06", "ERROR: FAMILY: US02: I12: Husband's birth date 2021-09-09 is after marriage date 2003-09-08"])
if __name__ == '__main__':
    unittest.main()