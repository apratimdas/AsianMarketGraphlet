import re
import operator

finaldict = {}
ctr = 1
pricelist = []
netprice = 0

edgelist = []
namelist = []
namedict = {}
dctr = 1

total_pre_calc = 35104419583987
threshold = int(total_pre_calc*0.9)

with open("test-combined.txt", "r") as ins:
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
# print(len(edgelist))

# print(finaldict)

sorted_d = sorted(finaldict.items(), key=operator.itemgetter(1), reverse=True)

while threshold < total_pre_calc:
    threshold += sorted_d[-1][1]
    finaldict.pop(sorted_d[-1][0])
    # print("deleted " + str(sorted_d[-1]))
    del sorted_d[-1]
    sorted_d.pop()

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


for edge in finaldict:
    print(str(edge[0]) + " " + str(edge[1]))    