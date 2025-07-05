import requests
from IDdict import warehouseIDs
from URLdict import URLs

print("Для авторизации и дальнейшей работы введите специальный токен\n"
              "--------------------------------------------")
token = str(input())
HEADER = {'Authorization' : token}
print("Введите наименования склада\n"
      "--------------------------------------------")
whname = str(input())
while whname not in warehouseIDs:
    print("Кажется, такого склада не существует. Попробуйте снова\n"
            "--------------------------------------------")
    whname = str(input())
wh_id = warehouseIDs[whname]
getid = requests.get(URLs["koeficient"], headers=HEADER, params="warehouseIDs=120762")
idlist = getid.json()
length = len(idlist)
print(f"{wh_id}")
# for i in range(length):
#     if idlist[i]['boxTypeName'] == "Короба":
#         print(idlist[i])