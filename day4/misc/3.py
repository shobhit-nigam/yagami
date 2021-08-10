import difflib

listx = ['aa', 'bb', 'cc', 'dd']
listy = ['aa', 'be', 'cc', 'ee']

for d in difflib.ndiff(listx, listy):
    print(d)
