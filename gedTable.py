from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
import datetime
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable
from collections import OrderedDict
from individual import individual as indiClass
from family import family
import sys
import warnings

def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def from_dob_to_death(born,death):
    return death.year - born.year - ((death.month, death.day) < (born.month, born.day))

def printTablesData(indiDict_obj, famDict_obj):
    indi = PrettyTable()
    family = PrettyTable()

    indi.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    family.field_names = ['ID','Married','Divorced','Husband ID', 'Husband Name', 'Wife ID','Wife Name', 'Children']

    for id in indiDict_obj:
        individualData = indiDict_obj[id]
        indi.add_row(individualData.Get_details())

    for id in famDict_obj:
        famData = famDict_obj[id]
        family.add_row(famData.Get_details())

    print("Individuals")
    print (indi)
    print("Families")
    print (family)
    return indi, family


def processGEDCOM(file_path):
  
    gedcom_parser = Parser()

    gedcom_parser.parse_file(file_path)

    root_elements = gedcom_parser.get_element_list()

    info = {"INDI": [], "FAM":[]}

    for element in root_elements:
       if str(element.get_tag()) == "INDI" or str(element.get_tag()) =="FAM":
           if element.get_tag() == "INDI" and len(info[element.get_tag()]) > 5000:
               raise ValueError("Too many individuals in file")
           if element.get_tag() == "FAM" and len(info[element.get_tag()]) >1000:
               raise ValueError("Too many families in file")

    months = {"JAN" : 1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEP":9,"OCT":10,"NOV":11, "DEC":12}

    indiDict = OrderedDict()
    myTag = ""

    famDict = OrderedDict()
    famTag = ""
    isMarried = False
    isDivorced = False
    for element in root_elements:
        age = 0


        if(element.get_level() == 0 and element.get_tag() == "INDI"):
            individualString = element.to_gedcom_string()
            individualString = individualString.replace('@','').strip().split(" ")

            myTag = individualString[1]

            indiDict[myTag] = indiClass(myTag)
            indiDict[myTag].Set_ID(myTag)

        if (element.get_level() == 1) and element.get_tag() == "FAMC" :
            childString = element.to_gedcom_string()
            childString = childString.replace('@','').strip().split(" ")
            indiDict[myTag].Set_child(childString[2])

        if (element.get_level() == 1) and element.get_tag() == "FAMS" :
            spouseString = element.to_gedcom_string()
            spouseString = spouseString.replace('@','').strip().split(" ")
            indiDict[myTag].Set_spouse(spouseString[2])

        if isinstance(element, IndividualElement):

            (first, last) = element.get_name()
            indiDict[myTag].Set_name(str(first+ " " +last))

            indiDict[myTag].Set_gender(element.get_gender())

            
            if(element.is_deceased() == True):

                indiDict[myTag].Set_alive(False)

                bday = element.get_birth_data()[0]
                death = element.get_death_data()[0]

                bday = bday.split(" ")
                bday = datetime.date(int(bday[2]),int(months[bday[1]]), int(bday[0]))
                death = death.split(" ")
                death = datetime.date(int(death[2]),int(months[death[1]]), int(death[0]))

                
                indiDict[myTag].Set_birthday(bday)
                indiDict[myTag].Set_death(death)
                age = from_dob_to_death(bday, death)
                indiDict[myTag].Set_age(age)

            else:
                indiDict[myTag].Set_alive(True)
                bday = element.get_birth_data()[0].split(" ")
                bday = datetime.date(int(bday[2]),int(months[bday[1]]), int(bday[0]))
                indiDict[myTag].Set_birthday(bday)
                age = from_dob_to_age(bday)
                indiDict[myTag].Set_age(age)

        if(element.get_level() == 0 and element.get_tag() == "FAM"):
            familyString = element.to_gedcom_string()
            familyString = familyString.replace('@','').strip().split(" ")
            famTag = familyString[1]
            famDict[famTag] = family(famTag)
            famDict[famTag].Set_ID(famTag)
        if(element.get_level() == 1 and element.get_tag() == "MARR"):
            isMarried = True
        if(isMarried and element.get_tag()=="DATE" and element.get_level()==2):
            marriedDay = element.get_value()
            marriedDay = marriedDay.split(" ")
            marriedDay = datetime.date(int(marriedDay[2]),int(months[marriedDay[1]]), int(marriedDay[0]))
            famDict[famTag].Set_married(marriedDay)
            isMarried = False
        if(element.get_tag()=="DIV" and element.get_level()==1):
            isDivorced = True
        if(isDivorced and element.get_tag()=="DATE" and element.get_level()==2):
            divorcedDay = element.get_value()
            divorcedDay = divorcedDay.split(" ")
            divorcedDay = datetime.date(int(divorcedDay[2]),int(months[divorcedDay[1]]), int(divorcedDay[0]))
            famDict[famTag].Set_divorced(divorcedDay)
            isDivorced = False
        if(element.get_level()==1 and element.get_tag()=="HUSB"):
            husbStr = element.to_gedcom_string()
            husbStr = husbStr.replace('@','').strip().split(" ")[2]
            famDict[famTag].Set_husbandID(husbStr)
            famDict[famTag].Set_husbandName(indiDict[husbStr].Get_name())
        if(element.get_level()==1 and element.get_tag()=="WIFE"):
            wifeStr = element.to_gedcom_string()
            wifeStr = wifeStr.replace('@','').strip().split(" ")[2]
            famDict[famTag].Set_wifeID(wifeStr)
            famDict[famTag].Set_wifeName(indiDict[wifeStr].Get_name())
        if(element.get_level()==1 and element.get_tag()=="CHIL"):
            child = element.to_gedcom_string()
            child = child.replace('@','').strip().split(" ")[2]
            famDict[famTag].Set_children(child)

    return indiDict, famDict

if __name__ == "__main__":
    individuals, families = processGEDCOM("AkhileshReddyFamily.ged")
    sys.stdout = open("FamilyTree.txt", "w")
    printTablesData(individuals, families)
    sys.stdout.close()