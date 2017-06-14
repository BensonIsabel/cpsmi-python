import string
import random


def hitriiparser(inputstring: str):
    outlist = []
    templist = []
    moyaborba = string.punctuation + " " + "«" + "»" + "“" + "„"

    for x in range(len(inputstring)):
        if inputstring[x] in moyaborba:
            if templist:
                outlist.append(templist)
                templist.clear()
            outlist.append([inputstring[x]])
        else:
            templist.append(inputstring[x])
    if templist:
        outlist.append(templist)
    return outlist


def hitriishuffle(inputlist: list):
    random.seed()

    for x in range(len(inputlist)):
        if len(inputlist[x]) > 3:
            tmplist = inputlist[x][1:-1]
            random.shuffle(tmplist)
            inputlist[x][1:-1] = tmplist
    return inputlist


def hitriilisttostring(inputlist: list):
    for x in range(len(inputlist)):
        inputlist[x] = "".join(inputlist[x])
    return "".join(inputlist)


instring = input('Enter some quote: ')
print(hitriilisttostring(hitriishuffle(hitriiparser(instring))))
