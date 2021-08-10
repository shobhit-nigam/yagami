import re

fa = open("data.txt", "r")

stra = fa.read()

pat = '\d+'

res = re.findall(pat, stra)

print(res)
