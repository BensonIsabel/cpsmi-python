import distance
import time

# instringa = input('Enter First string: ')
# instringb = input('Enter Second string: ')


def ldistance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n+1)
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1, n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

# print("Levenshtein length = ", ldistance(instringa, instringb))
# print("Levenshtein quick length = ", distance.quick_levenshtein(instringa, instringb))


def test(funcname):

    l = ['Print', 'Yesterday', 'All', 'my', 'troubles' 'seemed so far away',
         'Now it looks as though they', 're here to stay',
         'Oh, I believe in yesterday',
         'Suddenly,',
         'I', 'm not half the man I used to be',
         'There', 's a shadow hanging over me',
         'Oh, yesterday came suddenly']

    starttime = time.time()

    for i in range(0, 1000):
        for j in range(len(l) - 1):
            funcname(l[j], l[j+1])

    endtime = time.time()

    return endtime - starttime


t1 = test(ldistance)
t2 = test(distance.quick_levenshtein)
t3 = test(distance.levenshtein)
print("test: \n  My Distance: ", t1, "sec")
print("test: \n  Module  FastDistance: ", t2, "sec")
print("test: \n  Module  Distance: ", t2, "sec")