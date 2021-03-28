from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta



def userStory05(file):
    indiDict,famDict = processGEDCOM(file)
    wife_status = False
    men_status = False
    resultList = list()


    for key in famDict:
        family = famDict[key]
        familyID = family.Get_ID()

        if(famDict[key] != 'NA'):
            husbandID = str(famDict[familyID].Get_husbandID())
            wifeID = str(famDict[familyID].Get_wifeID())
            if(husbandID != 'NA' and wifeID != 'NA'):
                if(indiDict[husbandID].Get_death() != 'NA'):
                    husbandDeath = indiDict[husbandID].Get_death()
                    men_status = True
                    
                if(indiDict[wifeID].Get_death() != 'NA'):
                    wifeDeath = indiDict[wifeID].Get_death()
                    wife_status = True
                    
                if(famDict[familyID].Get_married() != "NA"):
                    marriedDate = famDict[familyID].Get_married()

                if(wife_status and marriedDate>wifeDeath):
                    result_1_str = f"ERROR: FAMILY: US05: The wedding occurs after wife death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Wife Death: " + str(wifeDeath)
                    resultList.append(result_1_str)

                if(men_status and marriedDate>husbandDeath):
                    result_1_str = f"ERROR: FAMILY: US05: The wedding occurs after husband death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Husband Death: " + str(husbandDeath)
                    resultList.append(result_1_str)

    return resultList


if __name__ == "__main__":
    print(userStory05("AkhileshreddyFamily_US5_02.ged"))
