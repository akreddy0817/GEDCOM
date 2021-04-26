from individual import individual
from gedTable import processGEDCOM
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta

'''
US21:Correct gender for role


'''

def userStory23(file):

    indiDict, famDict = processGEDCOM(file)
    indiList = []
    resultList = list()

    for index in indiDict:
        indiList += [index]

    count = 0
    while count <= len(indiList)-2:
        tempIndi1 = indiDict[indiList[count]]

        temp = count + 1
        while temp <= len(indiList)-1:
            tempIndi2 = indiDict[indiList[temp]]
            if tempIndi1.Get_name() == tempIndi2.Get_name() and tempIndi1.Get_birthday() == tempIndi2.Get_birthday():
                indi_1 = tempIndi1.Get_ID()
                indi_2 = tempIndi2.Get_ID()
                indiBirth_2 = tempIndi2.Get_birthday()
                indiName_2 = tempIndi1.Get_name()
                resultList.append(f"ERROR: INDIVIDUAL: US23: Two individuals have duplicate names and birthdays [{tempIndi1.Get_name()}, {tempIndi2.Get_birthday()}].")
            temp += 1
        count += 1

    resultList.sort()
    # print_list(resultList);
    return resultList
if __name__ == "__main__":
    print(userStory23("AkhileshReddyFamily_US23_01.ged"))