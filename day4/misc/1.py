import difflib

listx = ['aa', 'bb', 'cc', 'dd']
listy = ['aa', 'gg', 'cc', 'ee']

for d in difflib.context_diff(listx, listy):
    print(d)
