import re
hand = open('clown.txt')
for line in hand:
    line = line.rstrip()
    if re.search('$the', line):
        print(line)