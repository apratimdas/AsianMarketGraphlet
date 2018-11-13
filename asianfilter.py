import re
import operator

enumclass = []

finaldict = {}
ctr = 1
pricelist = []
netpricet = 0
netprice = 0

filename = "test-combined1995.txt"

edgelist = []
namelist = []
namedict = {}
dctr = 1

total_pre_calc = 0

with open(filename, "r", encoding='utf-16') as ins:
    namelisttemp = []
    for line in ins:
        # print(line)
        valctr = 0
        value = re.findall(': [0-9]*', line)
        for val in value:
            # print(val)
            valctr = int(val[2:])
            # print(valctr)
            netpricet += valctr

# print(netpricet)
# input("enter")
total_pre_calc = netpricet
threshold = int(netpricet*0.9)

anamelist = []
with open("asianlist.txt", "r") as ins:
    for line in ins:
        anamelist.append(line[:-1])


with open(filename, "r", encoding='utf-16') as ins:
    namelist = []
    for line in ins:
        valctr = 0
        value = re.findall(': [0-9]*', line)
        for val in value:
            valctr = int(val[2:])
            netprice += valctr
        if(len(value) == 0):
            continue

        idx = line.find('-->')
        if idx == -1:
            idx = line.find('<--')
        
        vertex_a = line[0:idx-1]
        vertex_b = line[idx+4:line.find(':')-1]
        # vertex_a = re.findall(".*[><-]", line)[0][:-4]
        # vertex_b = re.findall('[><-].* : ',line)[0][4:-3]
        if vertex_a not in anamelist and vertex_b not in anamelist:
            continue
        # print(str(vertex_a) + ' -- ' + str(vertex_b))
        temp = []
        i1 = 0
        i2 = 0
        if vertex_a in namelist:
            i1 = namedict[vertex_a]
        else:
            namelist.append(vertex_a)
            namedict[vertex_a] = dctr
            i1 = dctr
            dctr += 1

        if vertex_b in namelist:
            i2 = namedict[vertex_b]
        else:
            namelist.append(vertex_b)
            namedict[vertex_b] = dctr
            i2 = dctr
            dctr += 1

        edge = tuple(sorted([i1, i2]))
        if edge in finaldict:
            finaldict[edge] += valctr
        else:
            finaldict[edge] = valctr
        
        if(vertex_a < vertex_b):
            temp.append(vertex_a)
            temp.append(vertex_b)
        else:
            temp.append(vertex_b)
            temp.append(vertex_a)

        edgelist.append(temp)

# print(netprice)


# print(len(edgelist))
edgelist = set(tuple(row) for row in edgelist)
print(len(namelist))

# print(finaldict)

sorted_d = sorted(finaldict.items(), key=operator.itemgetter(1), reverse=True)

delcount = 0

while threshold < total_pre_calc:
    threshold += sorted_d[-1][1]
    finaldict.pop(sorted_d[-1][0])
    # print("deleted " + str(sorted_d[-1]))
    del sorted_d[-1]
    delcount += 1
    sorted_d.pop()

# print(delcount)
# input("enter")

uniquenodelist = []
for edge in finaldict:
    if edge[0] not in uniquenodelist:
        uniquenodelist.append(edge[0])
    if edge[1] not in uniquenodelist:
        uniquenodelist.append(edge[1])


todel = []

for edge in finaldict:
    if edge[0] == edge[1]:
        todel.append(edge)

for edge in todel:
    finaldict.pop(edge)


uniqueedges = []


# print(anamelist)
for edge in finaldict:
    if edge not in uniqueedges:
        edgeswap = []
        edgeswap.append(edge[1])
        edgeswap.append(edge[0])
        if edgeswap not in uniqueedges:
            uniqueedges.append(edge)

for edge in uniqueedges:
    print(str(edge[0]) + " " + str(edge[1]))