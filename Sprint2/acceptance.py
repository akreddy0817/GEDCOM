from gedTable import printTable
from gedTable import processGEDCOM
from userStory5 import userStory05
from userStory6 import userStory06
from userStory7 import userStory07
from userStory8 import userStory08

def sprint2_results():
	fileName="sprint2_Reddy.ged"
	idict,famdict = processGEDCOM(fileName)
	indiTable,familyTable= printTable(idict, famdict)
	errors = []
	errors.extend(userStory05("sprint2_Reddy.ged"))
	errors.extend(userStory06("sprint2_Reddy.ged"))
	errors.extend(userStory07("sprint2_Reddy.ged"))
	errors.extend(userStory08("sprint2_Reddy.ged"))

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
    sprint2_results()