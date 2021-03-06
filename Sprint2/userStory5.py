from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta



def userStory05(file):
    i_dict,fam_dict = processGEDCOM(file)
    wife_status = False
    men_status = False
    errors = list()


    for key in fam_dict:
        family = fam_dict[key]
        fam_id = family.Get_ID()

        if(fam_dict[key] != 'NA'):
            h_id = str(fam_dict[fam_id].Get_husbandID())
            w_id = str(fam_dict[fam_id].Get_wifeID())
            if(h_id != 'NA' and w_id != 'NA'):
                if(i_dict[h_id].Get_death() != 'NA'):
                    husbandDeath = i_dict[h_id].Get_death()
                    men_status = True
                    
                if(i_dict[w_id].Get_death() != 'NA'):
                    wifeDeath = i_dict[w_id].Get_death()
                    wife_status = True
                    
                if(fam_dict[fam_id].Get_married() != "NA"):
                    marriedDate = fam_dict[fam_id].Get_married()

                if(wife_status and marriedDate>wifeDeath):
                    result_1_str = f"ERROR: FAMILY: US05: Wedding " +str(fam_dict[fam_id].Get_married()) +  " occurs after Wife death " + str(wifeDeath) + "." 
                    errors.append(result_1_str)

                if(men_status and marriedDate>husbandDeath):

                    result_1_str = f"ERROR: FAMILY: US05: Wedding " +str(fam_dict[fam_id].Get_married()) +  " occurs after Husband death " + str(husbandDeath) + "." 
                    errors.append(result_1_str)

    return errors


if __name__ == "__main__":
    print(userStory05("AkhileshreddyFamily_US5_01.ged"))
