print("Enter some string>> ")
strng = str(input())
for x in range(len(strng)):
    print(strng[-(x+1)], end="")
