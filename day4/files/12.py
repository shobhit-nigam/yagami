import os

for x in os.walk('/Users/shobhit/Desktop/qualcomm/day2'):
    print(x[0])     # root path
    print(x[1])     # list of folders
    print(x[2])     # list of files
    print("----")
