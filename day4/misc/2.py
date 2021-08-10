import difflib

listx = ['aa', 'bb', 'cc', 'dd']
listy = ['aa', 'bb', 'cc', 'ee']

for d in difflib.context_diff(listx, listy):
    print(d)
