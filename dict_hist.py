from typing import Dict, Any, Union

count = dict()
names = ['kiki', 'muppy', 'shammu', 'kiki']
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)

print('---------New get()----------------')

jam: dict[str, Union[int, Any]] = dict()
names = ['kiki', 'muppy', 'shammu', 'kiki']
for name in names:
    jam[name] = jam.get(name, 0) + 1
print(jam)