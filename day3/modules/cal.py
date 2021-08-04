import sys

val = None
if not len(sys.argv) == 4:
    print("mismatch in number of arguments")
elif (sys.argv[2] == '-'):
    val = float(sys.argv[1]) - float(sys.argv[3])
elif (sys.argv[2] == '+'):
    val = float(sys.argv[1]) + float(sys.argv[3])
elif (sys.argv[2] == '*'):
    val = float(sys.argv[1]) * float(sys.argv[3])
elif (sys.argv[2] == '/'):
    val = float(sys.argv[1]) / float(sys.argv[3])
else:
    print("something went wrong")

print(sys.argv[1], sys.argv[2], sys.argv[3], "=", val)
