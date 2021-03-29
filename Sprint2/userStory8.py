from individual import individual
from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta

'''
US08
Children should be born after marriage of parents (and not more than 9 months after their divorce)
'''

def userStory08(file):
    i_dict, f_dict = processGEDCOM(file)
    errors = list()

    for key in f_dict:
        family = f_dict[key]

        if(family.Get_ID() != 'NA'):
            children = family.Get_children()

            if children != 'NA':
                child_list = [i for i in i_dict.values() if i.Get_ID() in children]

                for child in child_list:
                    child_birth = child.Get_birthday()

                    if (family.Get_divorced() != 'NA'):
                        divorce = family.Get_divorced()
                        divorce_birth_limit = datetime.timedelta(seconds=(9*4*7*24*60*60))

                        if ((child_birth-divorce) > divorce_birth_limit):
                            result_1_str = f"ERROR: FAMILY: US08: Child's birthday occurs more than 9 months after parents' divorce. ID: {family.Get_ID()} Child's birthday: {child_birth} Parents' divorce date: {divorce}"
                            errors.append(result_1_str)
                    elif (family.Get_married() != 'NA'):
                        marriage = family.Get_married()
                        
                        if (child_birth < marriage):
                            result_2_str = f"ERROR: FAMILY: US08: Child's birthday occurs before parents' marriage. ID: {family.Get_ID()} Child's birthday: {child_birth} Parents' marriage date: {marriage}"
                            errors.append(result_2_str)

    return errors


if __name__ == "__main__":
    print(userStory08("AkhileshReddyFamily_US08_02.ged"))
