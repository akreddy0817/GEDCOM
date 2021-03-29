import unittest
from datetime import datetime
from userStory7 import userStory07

class TestUserStory07Class(unittest.TestCase):
    now = datetime.now().date()

    def testUserStory07_1(self):
        results = userStory07("AkhileshReddyFamily.ged", self.now)
        self.maxDiff = None
        self.assertEqual(results, [])
    
    def testUserStory07_2(self):
        results = userStory07("AkhileshReddyFamily_US07_01.ged", self.now)
        self.maxDiff = None
        self.assertEqual(results, [
            "ERROR: INDIVIDUAL: US07: Person's death occurs more than 150 years after birth. ID: I5 Birth date: 1925-10-07 Death date: 2320-04-13"
        ])

    def testUserStory07_3(self):
        results = userStory07("AkhileshReddyFamily_US07_02.ged", self.now)
        self.maxDiff = None
        self.assertEqual(results, [
            "ERROR: INDIVIDUAL: US07: Person's death occurs more than 150 years after birth. ID: I5 Birth date: 1925-10-07 Death date: 2320-04-13",
            f"ERROR: INDIVIDUAL: US07: Current date is more than 150 years after person's birth. ID: I9 Birthdate: 1765-10-11 Current date: {self.now}"
        ])


if __name__ == '__main__':
    unittest.main()
