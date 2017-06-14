# import random
#
# print("enter length>> ")
# random.seed()
# n = int(input())
# list = [(random.randint(-10, 10)/10) for x in range(n)]
list = [8, 2, 2.5, 3, -5]


print(list)
index = [list.index(min(list)), list.index(max(list))]
index.sort()
psw3 = list[index[0] + 1:index[1]]
print(list)
for i in range(len(psw3)):
    if not float(psw3[i]).is_integer():
        psw3[i] = 0
print(psw3)
print(sum(psw3))
