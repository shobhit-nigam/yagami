avengers = {'thor':'hammer', 'captain':['shield', 'hammer'], 'ironman':'suit', 'wanda':'power'}
xmen = ['mystique', 'wolverine', 'magneto']
marvel = {1:avengers, 2:xmen}
print(marvel)
print("----")
print(marvel[1])
print("----")
print(marvel[1]['captain'])
print("----")
print(marvel[1]['captain'][1])
print("----")
print(marvel[1]['captain'][1][2])
