import re

fa = open("data.txt", "r")

stra = fa.read()

pat = '\d{3}'

res = re.findall(pat, stra)

print(res)
