from individual import individual
from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta

'''
US09: Birth before death of parents
'''


def userStory09(file):

   
    individuals, families = processGEDCOM(file)
    resultsList = list()

    for family_id, family in families.items():

        if family.Get_married() != "NA":

            husband = family.Get_husbandID()
            wife = family.Get_wifeID()
        
            husband_date = individuals[husband].Get_death()
            wife_date = individuals[wife].Get_death()

            children = family.Get_children()

            if len(children) > 0 and (wife_date != "NA" and husband_date != "NA"):
                for child in children:
                    child_birthdate = individuals[child].Get_birthday()
                    if husband_date < child_birthdate:            
                        resultsList.append(f"ERROR: FAMILY: US09: {family_id}: Husband ({husband}) died {husband_date} before child's ({child}) birth {child_birthdate}")
                    if wife_date < child_birthdate:
                        resultsList.append(f"ERROR: FAMILY: US09: {family_id}: Wife ({wife}) died {wife_date} before child's ({child}) birth {child_birthdate}")

    return resultsList

if __name__ == "__main__":
    print(userStory09("sprint3_Reddy.ged"))