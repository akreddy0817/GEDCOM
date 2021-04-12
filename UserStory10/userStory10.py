from individual import individual
from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta

'''
US09: Marriage after 14
'''


def userStory10(file):

   
    individuals, families = processGEDCOM(file)
    resultsList = list()

    for family_id, family in families.items():

        if family.Get_married() != "NA":

            husband = family.Get_husbandID()
            wife = family.Get_wifeID()

            husband_date = individuals[husband].Get_birthday()
            wife_date = individuals[wife].Get_birthday()

            family_marriage_date = family.Get_married()
            if float(relativedelta(family_marriage_date, husband_date).years) < float(14):
                resultsList.append(f"ERROR: FAMILY: US10: {family_id}: Husband ({husband}) birth date {husband_date} not at least 14 years prior to marriage date {family_marriage_date}")
            if float(relativedelta(family_marriage_date, wife_date).years) < float(14):
                resultsList.append(f"ERROR: FAMILY: US10: {family_id}: Wife ({wife}) birth date {wife_date} not at least 14 years prior to marriage date {family_marriage_date}")
    
    return resultsList
if __name__ == "__main__":
    print(userStory10("AkhileshReddyFamily_US10_01.ged"))