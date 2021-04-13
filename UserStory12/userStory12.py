from individual import individual
from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta

'''
US12:Parents not too old

'''


def userStory12(file):

    individuals, families= processGEDCOM(file)
    resultsList = list()


    for user_id in individuals.items():

        user_id = user_id[0]
        children_fam = individuals[user_id].Get_spouse()
        if children_fam == "NA":
            continue
        gender = individuals[user_id].Get_gender()
        parent_bday = individuals[user_id].Get_birthday()
        for each in children_fam:
            if families[each].Get_children() == 'NA':
                continue
            for child in families[each].Get_children():
                child_bday = individuals[child].Get_birthday()
                if gender == 'M':
                    datediff = rdelta.relativedelta(child_bday,parent_bday)
                    if datediff.years >=80:
                        resultsList.append(f"ERROR: INDIVIDUAL: US12: {user_id}: Father {user_id} is more than 80 years older than his child ({child}): {individuals[child].Get_name()}.")
                else:
                    datediff = rdelta.relativedelta(child_bday,parent_bday)
                    if datediff.years >=60:
                        resultsList.append(f"ERROR: INDIVIDUAL: US12: {user_id}: Mother {user_id} is more than 60 years older than her child ({child}): {individuals[child].Get_name()}.")
    resultsList.sort()
  
    return resultsList






if __name__ == "__main__":
    print(userStory12("AkhileshReddyFamily_US12_01.ged"))