fa = open("bojack.txt", "r")
fb = open("horseman.txt", "w")

stra = fa.read()

lista = stra.split()

for w in lista:
    fb.write(w+"\n")

fa.close()
fb.close()
