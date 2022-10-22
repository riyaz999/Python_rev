count = dict()
names = ['kiki', 'muppy', 'shammu', 'kiki']
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)
