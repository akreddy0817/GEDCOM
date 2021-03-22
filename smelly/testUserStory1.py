import unittest
from userStory1 import userStory01


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
    

if __name__ == '__main__':
    unittest.main()