count = {'chuck': 1, 'fred': 99, 'jan': 200}
print(count['chuck'])
for key in count:
    print(key, count[key])
print(list(count))
print(count.keys())
print(count.values())
print(count.items())
