fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)
kiki = dict()
for w in hand:
    line = w.rstrip()
    line = line.split()
    for i in line:
        kiki[i] = kiki.get(i, 0) + 1
largest = -1
theword = None
for k, v in kiki.items():
    if v > largest:
        largest = v
        theword = k
print(theword, largest)
