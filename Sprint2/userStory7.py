from individual import individual
from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta

'''
US07: Less than 150 years old
Death should be less than 150 years after birth for dead people, and current date should be less than 150 years after birth for all living people
'''

def userStory07(file, current_time=datetime.datetime.now().date()):
    i_dict, _ = processGEDCOM(file)
    errors = list()

    for key in i_dict:
        individual = i_dict[key]

        if(individual.Get_ID() != 'NA'):
            diff_limit = datetime.timedelta(seconds=(150*365*24*60*60))
            birth = individual.Get_birthday()

            if (individual.Get_death() != 'NA'):
                death = individual.Get_death()

                if ((death-birth) > diff_limit):
                    result_1_str = f"ERROR: INDIVIDUAL: US07: Person's death occurs more than 150 years after birth. ID: {individual.Get_ID()} Birth date: {birth} Death date: {death}"
                    errors.append(result_1_str)
            else:
                if ((current_time-birth) > diff_limit):
                    result_2_str = f"ERROR: INDIVIDUAL: US07: Current date is more than 150 years after person's birth. ID: {individual.Get_ID()} Birthdate: {birth} Current date: {current_time}"
                    errors.append(result_2_str)

    return errors


if __name__ == "__main__":
    print(userStory07("AkhileshReddyFamily_US7_02.ged", datetime.now()))
