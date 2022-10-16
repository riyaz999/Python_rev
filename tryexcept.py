astr = 'hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print(istr, 'first')

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1
print(istr, 'second')