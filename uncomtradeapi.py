# https://comtrade.un.org/data/doc/api/#DataRequests

import urllib
import requests
import json

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

url3 = "https://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=HS&ps=2016&r=699%2C156%2C586%2C392%2C50&p=all&rg=all&cc=TOTAL&fmt=csv"


testurl = "http://comtrade.un.org/api/refs/da/view?type=C&freq=M&ps=201607&px=HS"

print("Calling API...")

reporteriddata = requests.get("https://comtrade.un.org/data/cache/reporterAreas.json").json()


# response = requests.get(url3)

# for item in data:
#     print(item)

# print(response.content)

