from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta



def userStory06(file):
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
                   
                if(family[fam_id].Get_divorced() != "NA"):
                    divorcedDate = family[fam_id].Get_divorced()

                    if(wife_status and divorcedDate > wifeDeath):
                        result_1_str = f"ERROR: FAMILY: US06: divorce occurs after wife death. Divorce Date: " + str(family[fam_id].Get_divorced()) + " Wife Death: " + str(wifeDeath)
                        errors.append(result_1_str)

                    if(men_status and divorcedDate>husbandDeath):
                        result_1_str = f"ERROR: FAMILY: US06: divorce occurs after husband death. Divorce Date: " + str(family[fam_id].Get_divorced()) + " Husband Death: " + str(husbandDeath)
                        errors.append(result_1_str)
    return errors


if __name__ == "__main__":
    print(userStory06("AkhileshReddyFamily_US6_02.ged"))
