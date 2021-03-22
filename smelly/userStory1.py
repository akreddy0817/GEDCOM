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
function to compare the dates as this solution offers simplicity. 


Bad Smell 02: There's dplicated code in user story 1 and user story 2 with printing out the output the result list. The technique 
I used was to create a printing method that can be group together and used in both user stories and makes the code more readable. 
'''

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
                    marriage = current > marr
                    if(marriage == False):
                        result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Marriage {marr} occurs in the future"
                        resultList.append(result_1_str)
            for i in range(len(fam)):
                div = famtbl[fam[i]].Get_divorced()
                if(div != 'NA'):
                    divorced = current > div
                    if(divorced == False):
                        result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Divorce {div} occurs in the future"
                        resultList.append(result_1_str)
            bday = current > user.Get_birthday()
            if(bday == False):
                result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Birthday {user.Get_birthday()} occurs in the future"
                resultList.append(result_1_str)
            if(user.Get_death() != 'NA'): 
                death = current > user.Get_death()
                if(death == False):
                    result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Death {user.Get_death()} occurs in the future"
                    resultList.append(result_1_str)
    for i in resultList:
        print(i)
    return resultList


if __name__ == "__main__":
    print(userStory01("sprint1_Reddy.ged"))
