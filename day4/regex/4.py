import re

fa = open("data.txt", "r")

stra = fa.read()

pat = '\d+'
rep = '##'

res = re.sub(pat, rep, stra)

print(res)
