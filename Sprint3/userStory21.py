from individual import individual
from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta

'''
US21:Correct gender for role


'''


def userStory21(file):

    individuals, families = processGEDCOM(file)
    resultsList = list()

    for fam in families:
        
        fclass = families[fam]

        husb_id = fclass.Get_husbandID()
        wife_id = fclass.Get_wifeID()
        if husb_id != 'NA':
            male = individuals[husb_id].Get_gender()
            if male != 'M':
                resultsList.append(f"ERROR: FAMILY: US21: {fam}: Husband ({husb_id}) is labelled incorrectly as ({male}).")
        if wife_id != 'NA':
            female = individuals[wife_id].Get_gender()
            if female != 'F':
                resultsList.append(f"ERROR: FAMILY: US21: {fam}: Wife ({wife_id}) is labelled incorrectly as ({female}).")


    return resultsList

if __name__ == "__main__":
    print(userStory21("AkhileshReddyFamily_US21_02.ged"))