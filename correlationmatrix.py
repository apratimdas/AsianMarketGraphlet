
from numpy import *

gdv=[]

with open("wtn.out", "r") as ins:
    for line in ins:
        temp = line[:-1].split(" ")
        numbers = [int(x) for x in temp]
        gdv.append(numbers)

gdvt = [*zip(*gdv)]

gdvtarray = []
for i in gdvt:
    gdvtarray.append((list(i)))
    # print((list(i)))

gcm = corrcoef(gdvtarray)

for i in gcm:
    for j in i:
        print("{0:.2f}".format(j),end=',')
    print()

# print(gcm[0][0])

