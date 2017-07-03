import string
import random
from copy import copy


class MyMain:
    def __init__(self, inp: str):
        templist = []
        mypunc = string.punctuation + " " + "«" + "»" + "“" + "„"
        self.data = []
        result = []
        for x in range(len(inp)):
            if inp[x] in mypunc:
                if templist:
                    result.append(templist)
                    templist = []
                result.append([inp[x]])
            else:
                templist.append(inp[x])
        if templist:
            result.append(templist)
        self.data = result

    def __str__(self):
        result = copy(self.data)
        for x in range(len(result)):
            result[x] = "".join(result[x])
        return "".join(result)

    def myshuffle(self):
        random.seed()
        result = self.data
        for x in range(len(result)):
            if len(result[x]) > 3:
                print(result[x])
                tmplist = result[x][1:-1]
                random.shuffle(tmplist)
                result[x][1:-1] = tmplist
        self.data = result


text2 = MyMain("!!!Съешь же ещё этих мягких французских булок-то, да выпей-ка 12345667")
print(text2)
text2.myshuffle()
print(text2)
