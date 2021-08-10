import re

fa = open("data.txt", "r")

stra = fa.read()

pat = '\d{3}'

res = re.match(pat, stra)

if res:
    print("found")
else:
    print("not found")
