import datetime


objd = datetime.date.today()

print("year =", objd.year)

objn = datetime.datetime.now()

objt = objn.strftime("%m:%d:%Y")
print(objt)
