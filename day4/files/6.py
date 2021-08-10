fa = open("bojack.txt", "r")

stra = fa.read()

print(stra.splitlines())
print("----")
print(stra.split())

fa.close()
