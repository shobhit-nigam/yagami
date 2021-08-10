fa = open("bojack.txt", "r")

stra = fa.read(7)
stra = fa.read(7)

print(fa.tell())

fa.seek(4)
stra = fa.read(7)
print(stra)

fa.close()
