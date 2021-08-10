import pandas as pd

dfa = pd.read_csv("data.txt", sep=' ', header=None)
print(dfa)
dfb = dfa.sort_values(by=[2])
print("---")
print(dfb)
dfb.to_csv('new_data.txt', sep='\t', header=None, index=False)
