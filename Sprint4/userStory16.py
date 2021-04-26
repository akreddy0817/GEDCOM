from gedTable import processGEDCOM


'''
US16 - Male last names
All male members of a family should have the same last name
'''


def userStory16(file):
    individuals, families = processGEDCOM(file)
    resultsList = list()

    for fam in families.values():
        family_surname = fam.Get_husbandName().split(' ')[-1]
        children = fam.Get_children()

        for child_ID in children:
            if individuals[child_ID].Get_gender() == 'M':
                child_surname = individuals[child_ID].Get_name().split(' ')[-1]
                if child_surname != family_surname:
                    resultsList.append(f"ERROR: FAMILY: US16: Child {child_ID}\'s last name ({child_surname}) does not match family name ({family_surname}) in family {fam.Get_ID()}.")

    return resultsList


if __name__ == "__main__":
    print(userStory16("AkhileshReddyFamily.ged"))
