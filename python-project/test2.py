import requests
from IDdict import warehouseIDs
from URLdict import URLs

token = str(input("Token: "))
name = str(input("Warehouse name: "))
HEADER = {'Authorization' : token}
wh_id = warehouseIDs[name]
# test = requests.get(URLs['test'], headers=HEADER)
res = requests.get(URLs["warehouses"], headers=HEADER, params="warehouseIDs={wh_id}")
reslist = res.json()
for i in range(1000):
    if reslist[i]['name'] == name:
        print(reslist[i])
        break


# print(res.json())
# print(test.reason)
