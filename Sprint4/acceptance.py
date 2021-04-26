from gedTable import printTable
from gedTable import processGEDCOM
from userStory15 import userStory15
from userStory16 import userStory16
from userStory23 import userStory23
from userStory24 import userStory24

def sprint4_results():
	fileName="sprint4_Reddy.ged"
	idict,famdict = processGEDCOM(fileName)
	indiTable,familyTable= printTable(idict, famdict)
	errors = []
	errors.extend(userStory15(fileName))
	errors.extend(userStory16(fileName))
	errors.extend(userStory23(fileName))
	errors.extend(userStory24(fileName))

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
    sprint4_results()
