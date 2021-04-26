from gedTable import processGEDCOM


'''
US15 - Fewer than 15 siblings
There should be fewer than 15 siblings in a family
'''


def userStory15(file):
    individuals, families = processGEDCOM(file)
    resultsList = list()

    for fam in families.values():
        children = fam.Get_children()
        num_sibs = len(children)

        if children == "NA":
            continue

        if num_sibs >= 15:
            resultsList.append(f"ERROR: FAMILY: US15: Family {fam.Get_ID()} has {num_sibs} siblings.")

    return resultsList


if __name__ == "__main__":
    print(userStory15("AkhileshReddyFamily.ged"))
