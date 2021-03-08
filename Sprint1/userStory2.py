from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta

def userStory02(file):

    indiDict, famDict = processGEDCOM(file)
    
    resultList = list()

    for index in famDict:
        husbandID = famDict[index].Get_husbandID()
        wifeID = famDict[index].Get_wifeID()
    
        if wifeID != "NA":
            husBirthDate = indiDict[husbandID].Get_birthday()
        else: husBirthDate = "NA"
    
        if wifeID != "NA":
            wifeBirthDate = indiDict[wifeID].Get_birthday()
        else: wifeBirthDate = "NA"
    
        marriageDate = famDict[index].Get_married()
        
        if marriageDate != 'NA':
            if husBirthDate != 'NA':
                if husBirthDate > marriageDate:
                    result_1_str = f"ERROR: FAMILY: US02: {husbandID}: Husband's birth date {husBirthDate} is after marriage date {marriageDate}"
                    resultList.append(result_1_str)

            if wifeBirthDate != 'NA':
                if wifeBirthDate > marriageDate:
                    result_2_str = f"ERROR: FAMILY: US02: {wifeID}: Wife's birth date {wifeBirthDate} is after marriage date {marriageDate}"
                    resultList.append(result_2_str)

    return resultList

if __name__ == "__main__":
    print(userStory02("AkhileshReddyFamily_US2_05.ged"))
    '''
    print(userStory02("sprint1_Reddy.ged"))
    print(userStory02("AkhileshReddyFamily_US2_04.ged"))
    print(userStory02("AkhileshReddyFamily_US2_05.ged"))
    '''