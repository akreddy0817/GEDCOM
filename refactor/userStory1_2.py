from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta


'''
Bad Smell 01: There's repititive code by constantly comparing dates and storing the result in a variable. 
It's also not as readable and this configuration helps it make it easier to compute and read. To solve this, I created a 
function to compare 


Bad Smell 02: There's repititive output of printing the resultList() so need a function just for one call for both stories.

'''
def print_the_list(lst):
    for i in lst:
        print(lst)

def is_date1_older(date1, date2):
    return date1 > date2


def userStory01(file):
    info, famtbl = processGEDCOM(file)
    resultList = list()

    dt = datetime.datetime.now()
    current = datetime.date(dt.year, dt.month, dt.day)
    resultList = list()
    good = True
    
    for key in info:
        user = info[key]
        fam = user.Get_spouse()
        individualID = user.Get_ID()
        
        if fam != 'NA':
            for i in range(len(fam)):
                marr = famtbl[fam[i]].Get_married()
                if(marr != 'NA'):
                    if(is_date1_older(current, marr) == False):
                        result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Marriage {marr} occurs in the future"
                        resultList.append(result_1_str)
            for i in range(len(fam)):
                div = famtbl[fam[i]].Get_divorced()
                if(div != 'NA'):
                    if(is_date1_older(current, div) == False):
                        result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Divorce {div} occurs in the future"
                        resultList.append(result_1_str)
            bday = current > user.Get_birthday()
            if(is_date1_older(current, user.Get_birthday()) == False):
                result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Birthday {user.Get_birthday()} occurs in the future"
                resultList.append(result_1_str)
            if(user.Get_death() != 'NA'): 
                if(is_date1_older(current, user.Get_death()) == False):
                    result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Death {user.Get_death()} occurs in the future"
                    resultList.append(result_1_str)

    #print_the_list(resultList)
    return resultList


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
    print_the_list(resultList)
    return resultList

if __name__ == "__main__":
    print(userStory02("AkhileshReddyFamily_US2_03.ged"))
