from individual import individual
from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta



def userStory24(file):

    indiDict, famDict = processGEDCOM(file)
    famList = []
    resultList = list()

    for index in famDict:
        famList += [index]

    count = 0
    while count <= len(famList)-2:
        tempFam1 = famDict[famList[count]]
        tempFam1_Husb = tempFam1.Get_husbandName()
        tempFam1_Wife = tempFam1.Get_wifeName()
        temp = count + 1
        while temp <= len(famList)-1:
            tempFam2 = famDict[famList[temp]]
            tempFam2_Husb = tempFam2.Get_husbandName()
            tempFam2_Wife = tempFam2.Get_wifeName()
            if tempFam1_Husb == tempFam2_Husb and tempFam1_Wife == tempFam2_Wife:
                fam_1 = tempFam1.Get_ID()
                fam_2 = tempFam2.Get_ID()
                resultList.append(f"ERROR: FAMILY: US24: Two families [{fam_1}, {fam_2}] have duplicate spouses [{tempFam1_Husb}, {tempFam2_Wife}].")
            temp += 1
        count += 1

    resultList.sort()
    return resultList
if __name__ == "__main__":
    print(userStory24("AkhileshReddyFamily_US24_01.ged"))