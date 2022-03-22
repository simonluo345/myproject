from collections import Counter

newlist = []
with open("document.txt") as infile:

    for line in infile:
        split_it = line.lower().replace(',', '').replace('.', '').split()
        for i in split_it:
            newlist.append(i)
    print(newlist)


    newgood1 = Counter(newlist)
    mostcommon = newgood1.most_common(5)

for x,y in mostcommon:
    print(x, end=': ')
    print(y)
