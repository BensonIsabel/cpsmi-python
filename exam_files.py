def fprint(filename: str):
    try:
        f = open(filename)
        print(f.read())
        print("\n")
        f.close()
    except FileNotFoundError:
        print("no such a file:", filename)


def frevert(inp: str):
    try:
        inpf = open(inp)
        outfilename = "rev_" + inp
        outf = open(outfilename, "w")
        l = inpf.readlines()
        l.reverse()
        outf.writelines(l)
        inpf.close()
        outf.close()
    except FileNotFoundError:
            print("no such a file:", inp)


filename = "input.txt"
outfilename = "rev_" + filename
fprint(filename)
frevert(filename)
fprint(outfilename)
