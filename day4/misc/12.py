ga = 400

def funca():
    la = 30
    global ga
    ga = 300
    print("la =", la)
    print("ga =", ga)


print("outside ga =", ga)
funca()
print("outside ga =", ga)
