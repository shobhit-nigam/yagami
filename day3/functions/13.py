def funca(la, lb):
    return la+lb, la*lb, "hello"

varx = funca(100, 200)
print("varx =", varx)
print("----")
varx, vary, varz = funca(100, 200)
print("varx =", varx)
print("vary =", vary)
print("varz =", varz)
