
from numpy import corrcoef

gdv=[]

with open("test.out", "r") as ins:
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

gcmshuffle = []
gcmshuffle.append(gcm[9])
gcmshuffle.append(gcm[4])
gcmshuffle.append(gcm[6])
gcmshuffle.append(gcm[1])
gcmshuffle.append(gcm[12])
gcmshuffle.append(gcm[13])
gcmshuffle.append(gcm[2])
gcmshuffle.append(gcm[5])
gcmshuffle.append(gcm[11])
gcmshuffle.append(gcm[7])
gcmshuffle.append(gcm[8])
gcmshuffle.append(gcm[0])
gcmshuffle.append(gcm[3])
gcmshuffle.append(gcm[10])
gcmshuffle.append(gcm[14])

gcmshuffle2 = []
for i in range(0,15):
    gcmshuffle2.append([])

for i in range(0,15):
    gcmshuffle2[i].append(gcmshuffle[i][9])
    gcmshuffle2[i].append(gcmshuffle[i][4])
    gcmshuffle2[i].append(gcmshuffle[i][6])
    gcmshuffle2[i].append(gcmshuffle[i][1])
    gcmshuffle2[i].append(gcmshuffle[i][12])
    gcmshuffle2[i].append(gcmshuffle[i][13])
    gcmshuffle2[i].append(gcmshuffle[i][2])
    gcmshuffle2[i].append(gcmshuffle[i][5])
    gcmshuffle2[i].append(gcmshuffle[i][11])
    gcmshuffle2[i].append(gcmshuffle[i][7])
    gcmshuffle2[i].append(gcmshuffle[i][8])
    gcmshuffle2[i].append(gcmshuffle[i][0])
    gcmshuffle2[i].append(gcmshuffle[i][3])
    gcmshuffle2[i].append(gcmshuffle[i][10])
    gcmshuffle2[i].append(gcmshuffle[i][14])


for i in gcmshuffle2:
    for j in i:
        print("{0:.2f}".format(j),end=',')
    print()

# print(gcm[0][1])



