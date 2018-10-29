import re

dict = {}
ctr = 1
pricelist = []
netprice = 0

edgelist = []

total_pre_calc = 35104419583987

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
        vertex_a = re.findall('^.*[><-]', line)[0][:-4]
        vertex_b = re.findall('[><-].* : ',line)[0][4:-3]
        print(str(vertex_a) + ' -- ' + str(vertex_b))
        temp = []
        if(vertex_a < vertex_b):
            temp.append(vertex_a)
            temp.append(vertex_b)
        else:
            temp.append(vertex_b)
            temp.append(vertex_a)

        edgelist.append(temp)

print(netprice)


print(len(edgelist))
edgelist = set(tuple(row) for row in edgelist)
print(len(edgelist))

