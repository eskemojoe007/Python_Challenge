from itertools import groupby
# a = [1, 11, 21, 1211, 111221]

a = ['1']
for i in range(1, 31):
    word = []
    for key, group in groupby(a[i - 1]):
        counter = len(list(group))

        word.append(str(counter))
        word.append(key)

    a.append(''.join(word))

len(a[30])
# 5808
