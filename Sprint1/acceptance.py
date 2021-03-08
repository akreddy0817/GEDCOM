from gedTable import printTable
from gedTable import processGEDCOM
from userStory1 import userStory01
from userStory2 import userStory02
from userStory3 import userStory03
from userStory4 import userStory04

def sprint1_results():
	fileName="sprint1_Reddy.ged"
	indiObj,familyObj = processGEDCOM(fileName)
	indiTable,familyTable= printTable(indiObj, familyObj)
	errors = []
	errors.extend(userStory01(fileName))
	errors.extend(userStory02(fileName))
	errors.extend(userStory03(fileName))
	errors.extend(userStory04(fileName))

	for e in errors:
		print(e)

	with open('acceptance_results.txt','w') as file:
		file.write('Individuals Information--------------->\n')
		file.write(indiTable.get_string())
		file.write("\n\n\n")
		file.write('Family Information------------>\n')
		file.write(familyTable.get_string())
		file.write("\n\n")
		for e in errors:
			file.write(e+"\n")


if __name__ == "__main__":
    sprint1_results()