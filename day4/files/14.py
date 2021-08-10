with open("data.txt", "r") as fa:
    stra = fa.read()

lista = stra.splitlines()
col_c = []

for line in lista:
    col_c.append(int(line.split()[2]))

print(col_c)
