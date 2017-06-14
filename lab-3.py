import random


def generate(n):
    random.seed()
    return [(random.randint(-99, 99) / 10) for x in range(n)]


def task2(inpseq):
    ind = [inpseq.index(min(inpseq)), inpseq.index(max(inpseq))]
    ind.sort()
    tempseq = inpseq[ind[0] + 1:ind[1]]
    for i in range(len(tempseq)):
        if not float(tempseq[i]).is_integer():
            tempseq[i] = 0
    return int(sum(tempseq))


def task3(inpseq):
    if 0 in inpseq:
        inpseq.reverse()
        tempseq = list(filter(lambda x: x > 0, inpseq[0:inpseq.index(0)]))
        return sum(tempseq) / len(tempseq)
    else:
        return 0


seq = generate(1000000)
print(seq)
print('Сумма целых элементов последовательности, \nрасположенных между первыми минимальным и максимальным >> ', task2(seq), '\n')
print('Cреднее арифметическое положительных элементов, \nрасположенных после последнего нуля >> ', task3(seq))
