with open("data.txt", "r") as fa:
    stra = fa.read()

lista = stra.splitlines()
col_c = []

for line in lista:
    temp = line.split()
    col_c.append(temp[2])

print(col_c)
