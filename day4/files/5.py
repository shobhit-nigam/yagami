fa = open("bojack.txt", "r")

stra = fa.read()
print(stra)

print(stra.replace('good', 'nice'))

fa.close()
