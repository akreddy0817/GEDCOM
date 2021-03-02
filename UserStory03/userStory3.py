from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta


def userStory03(file):
    indiDict, famDict = processGEDCOM(file)
    resultList = list()

    for index in indiDict:
        personID = indiDict[index].Get_ID()
    
        if personID != "NA":
            personBirthDate = indiDict[personID].Get_birthday()
            personDeathDate = indiDict[personID].Get_death()

            if personBirthDate != 'NA' and personDeathDate != 'NA':
                if personBirthDate > personDeathDate:
                    result_str = f"ERROR: INDIVIDUAL: US03: : {personID}: Person's birth date {personBirthDate} is after death date {personDeathDate}"
                    resultList.append(result_str)
    
    return resultList


if __name__ == "__main__":
    print(userStory03("AkhileshReddyFamily_US3_03.ged"))
    print(userStory03("AkhileshReddyFamily_US3_04.ged"))
    print(userStory03("AkhileshReddyFamily_US3_05.ged"))
