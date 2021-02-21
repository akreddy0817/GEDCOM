## Akhilesh Reddy 
## I pledge my honor that I have abided by the Stevens Honor Systen.
def isValidTag(tag, level):
    valid_tag = {'INDI':0,'NAME':1,'SEX':1,'BIRT':1,'DEAT':1,'FAMC':1,'FAMS':1, 'FAM':0, 'MARR':1, 'HUSB':1,
            'WIFE':1,'CHIL':1, 'DIV':1, 'DATE':2, 'HEAD':0, 'TRLR':0, 'NOTE':0}
    try:
        return (valid_tag[tag] == int(level))
    except:
        return False

def gedcomPrgm(file):
    for line in file:
        print("--> "+line[:-1])
        string = line.split()
        args = ""
        for i in string[2:]:
            args += i + " "
        level = string[0]
        x = line.find("INDI")
        y = line.find("FAM")
        if(((x>=0) and level=='0') or ((y>=0) and level == '0')):
            tag = string[2]
            index = max(x,y)
            args = line[2:index]
        else:
            tag = string[1]
        if isValidTag(tag, level):
            valid = 'Y'
        else:
            valid = 'N'

        args = args[:-1]
        print("<-- " + level + "|" + tag + "|" + str(valid)[0] + "|"+ args)

if __name__ == "__main__":
    file = open("AkhileshReddyFamily.ged")
    gedcomPrgm(file)
