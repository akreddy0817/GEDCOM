from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta



def userStory06(file):
    indiDict,famDict = processGEDCOM(file)
    wife_status = False
    men_status = False
    errors = list()


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

                if(famDict[familyID].Get_divorced() != "NA"):
                    divorcedDate = famDict[familyID].Get_divorced()

                    if(wife_status and divorcedDate > wifeDeath):

                        result_1_str = f"ERROR: FAMILY: US06: Divorced " + str(famDict[familyID].Get_divorced()) + " after wife death " + str(wifeDeath) + "." 
                        errors.append(result_1_str)

                    if(men_status and divorcedDate>husbandDeath):
                        result_1_str = f"ERROR: FAMILY: US06: Divorced " + str(famDict[familyID].Get_divorced()) + " after husband death " + str(husbandDeath) + "." 
                        
                        errors.append(result_1_str)

    return errors

if __name__ == "__main__":
    print(userStory06("AkhileshReddyFamily_US6_02.ged"))
