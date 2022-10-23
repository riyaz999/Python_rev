d = {"a": 10, "d": 1000, "c": 4}
temp = list()
for i,j in d.items():
    temp.append((j,i))
print(temp)
kiki = sorted(temp, reverse=True)
print(kiki)