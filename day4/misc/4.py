import difflib
stra = "qualcomm"
listx = ['qaulcomm', 'kualqomm', 'qualcom', 'qti', 'kaulcom']

print(difflib.get_close_matches(stra, listx))
