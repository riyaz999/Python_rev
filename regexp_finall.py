import re
x = "my  2 favorite numbers are 19 and 42"
y = re.findall('[0-9]+', x)
print(y)