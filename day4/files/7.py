fa = open("bojack.txt", "r")

stra = fa.read()

print(fa.writable())
print(fa.closed)
fa.close()
print(fa.closed)
