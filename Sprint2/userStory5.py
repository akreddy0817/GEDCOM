from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta



def userStory05(file):
    i_dict,family = processGEDCOM(file)
    wife_status = False
    men_status = False
    errors = list()


    for key in family:
        family = family[key]
        fam_id = family.Get_ID()

        if(family[key] != 'NA'):
            h_id = str(family[fam_id].Get_h_id())
            w_id = str(family[fam_id].Get_w_id())
            if(h_id != 'NA' and w_id != 'NA'):
                if(i_dict[h_id].Get_death() != 'NA'):
                    husbandDeath = i_dict[h_id].Get_death()
                    men_status = True
                    
                if(i_dict[w_id].Get_death() != 'NA'):
                    wifeDeath = i_dict[w_id].Get_death()
                    wife_status = True
                    
                if(family[fam_id].Get_married() != "NA"):
                    marriedDate = family[fam_id].Get_married()

                if(wife_status and marriedDate>wifeDeath):
                    result_1_str = f"ERROR: FAMILY: US05: The wedding occurs after wife death. Wedding Date: " + str(family[fam_id].Get_married()) + " Wife Death: " + str(wifeDeath)
                    errors.append(result_1_str)

                if(men_status and marriedDate>husbandDeath):
                    result_1_str = f"ERROR: FAMILY: US05: The wedding occurs after husband death. Wedding Date: " + str(family[fam_id].Get_married()) + " Husband Death: " + str(husbandDeath)
                    errors.append(result_1_str)

    return errors


if __name__ == "__main__":
    print(userStory05("AkhileshreddyFamily_US5_02.ged"))
