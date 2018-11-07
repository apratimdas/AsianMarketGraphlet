# https://comtrade.un.org/data/doc/api/#DataRequests

import urllib
import requests
import json
import csv

# Add url data here
url = "http://comtrade.un.org/api/refs/da/view?type=C&freq=A&px=HS&ps=2016&p=all&r=all&max=49999&fmt=json"
url2 = "http://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=HS&ps=2016&r=all&p=all&rg=all&cc=AG2&fmt=csv"

"""
Dataset country codes for url3
India
China
Pakistan
Japan
Bangladesh
"""

url3 = "https://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=HS&ps=2016&r=699%2C156%2C586%2C392&p=all&rg=all&cc=TOTAL&fmt=csv"

temp = "https://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=HS&ps=2016&r=699%2C156%2C586%2C392%2C50&p=all&rg=all&cc=TOTAL&fmt=csv"

testurl = "http://comtrade.un.org/api/refs/da/view?type=C&freq=M&ps=201607&px=HS"

# print("Calling API...")

reporteriddata = requests.get("https://comtrade.un.org/data/cache/reporterAreas.json").json()

idlist = []

for id in reporteriddata['results']:
    idlist.append(id['id'])

idlist.remove(idlist[0])

# ctr=0
# for id in reporteriddata['results']:
#     if(id['id'] != '807'):
#         ctr+=1
#     else:
#         break

# newlist = idlist[ctr:]


idlistitr = 0

while idlistitr < len(idlist):
    idx1 = idlist[idlistitr]

    if(idlistitr+1 < len(idlist)):
        idx2 = idlist[idlistitr+1]
    else:
        idx2 = idx1
    if(idlistitr+2 < len(idlist)):
        idx3 = idlist[idlistitr+2]
    else:
        idx3 = idx1
    if(idlistitr+3 < len(idlist)):
        idx4 = idlist[idlistitr+3]
    else:
        idx4 = idx1

    specificurl = "https://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=HS&ps=1995&p=all&rg=all&cc=TOTAL&fmt=csv" + "&r=" + str(idx1) + "%2C" + str(idx2) + "%2C" + str(idx3) + "%2C" + str(idx4)
    print(specificurl)
    response = requests.get(specificurl)
    decoded_content = response.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        if(row[7] == 'Import'):
            print(row[9] + ' <-- ' + row[12] + ' : ' + row[-4])
        elif(row[7] == 'Export'):
            print(row[9] + ' --> ' + row[12] + ' : ' + row[-4])
        # else:
            # print(row[9] + ' -- ' + row[12])
    idlistitr += 4



# for id in idlist:
#     print("id : " + str(id))
#     specificurl = "https://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=HS&ps=2016&p=all&rg=all&cc=TOTAL&fmt=csv" + "&r=" + str(id)
#     print(specificurl)
#     response = requests.get(specificurl)
#     decoded_content = response.content.decode('utf-8')
#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
#         if(row[7] == 'Import'):
#             print(row[9] + ' <-- ' + row[12] + ' : ' + row[-4])
#         elif(row[7] == 'Export'):
#             print(row[9] + ' --> ' + row[12] + ' : ' + row[-4])
#         else:
#             print(row[9] + ' -- ' + row[12])


# response = requests.get(url3)
# decoded_content = response.content.decode('utf-8')
# cr = csv.reader(decoded_content.splitlines(), delimiter=',')
# my_list = list(cr)
# for row in my_list:
#     if(row[7] == 'Import'):
#         print(row[9] + ' <-- ' + row[12] + ' : ' + row[-4])
#     elif(row[7] == 'Export'):
#         print(row[9] + ' --> ' + row[12] + ' : ' + row[-4])
#     else:
#         print(row[9] + ' -- ' + row[12])


# print(response.content)

# for item in response.content:
#     print(item)

# print(response.content)

