avengers = ['captain', 'thor', 'black widow', 'hulk']
xmen = ['magneto', 'mystique', 'wolverine']
gaurdians = ['groot', 'star-lord', 'rocket', 'nebula']

print(avengers)
print("----")
avengers.append(xmen)
print(avengers)
print("----")
print(gaurdians)
#print("----")
gaurdians.extend(xmen)
print("----")
print(gaurdians)
gaurdians.extend('gamora')
print(gaurdians)
