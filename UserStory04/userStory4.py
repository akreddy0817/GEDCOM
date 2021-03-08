from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta

def userStory04(file):
    indiDict,famDict = processGEDCOM(file)
    resultList = list()

    for index in famDict:
        family = famDict[index]
        if (family.Get_divorced() == "NA"):
            continue
        divDate = family.Get_divorced()
        marrDate = family.Get_married()

        if (divDate < marrDate):
            error = f"ERROR: FAMILY: US04:{family.Get_ID()} Divorce date occurs before marriage date - Marriage {family.Get_married()}: Divorce {family.Get_divorced()}"
            resultList.append(error)
            continue


    resultList.sort()
    return resultList

if __name__ == "__main__":
    print(userStory04("AkhileshReddyFamily_US4_01.ged"))
