from collections import Counter

newlist = []
with open("document.txt") as infile:

    for line in infile:
        split_it = line.replace(',', '').replace('.', '').split()
        for i in split_it:
            newlist.append(i)

    newgood1 = Counter(newlist)
    mostcommon = newgood1.most_common(5)
    d = dict(mostcommon)
    r = sorted(d.items(), key=lambda x: (-x[1], x[0]))

for x,y in r:
    print(x, end=': ')
    print(y)


