varx = "hello"

listx = [print, type, len]

listx[0](varx)                  #print(varx)
listx[0](listx[2](varx))        #print(len(varx))
