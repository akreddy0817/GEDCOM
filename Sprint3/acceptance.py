from gedTable import printTable
from gedTable import processGEDCOM
from userStory9 import userStory09
from userStory10 import userStory10
#from userStory11 import userStory11
from userStory12 import userStory12

def sprint3_results():
	
	fileName="sprint3_Reddy.ged"
	idict,famdict = processGEDCOM(fileName)
	indiTable,familyTable= printTable(idict, famdict)
	errors = []
	errors.extend(userStory09(fileName))
	errors.extend(userStory10(fileName))
	#errors.extend(userStory11(fileName))
	errors.extend(userStory12(fileName))

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
    sprint3_results()