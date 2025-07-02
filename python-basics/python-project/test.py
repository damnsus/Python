import requests
import json
import pprint

testURL = 'https://content-api-sandbox.wildberries.ru/content/v2/object/parent/all'
postURL = "https://marketplace-api.wildberries.ru/api/v3/supplies"
plistURL = "https://marketplace-api.wildberries.ru/api/v3/supplies"

URLs = {'testURL' : ''}

testTOKEN = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQxMTE4djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTc0Nzc4NTgzNCwiaWQiOiIwMTkzNDQ0ZS1jOGQ1LTdhOGYtYTgyMC05Y2ZlYmZjODc1Y2YiLCJpaWQiOjEyNTMwMzM5Nywib2lkIjo0MTY1MjYxLCJzIjowLCJzaWQiOiJlNDJjZmQ5MS1kODNkLTRlNDMtYTQ0OS1iMjUxZWM0YjBkNWQiLCJ0Ijp0cnVlLCJ1aWQiOjEyNTMwMzM5N30.2CQmIMVpaZC8sz4Lw_Auw7ru4fe6tvDqXIYJOH2aHKc1WKoz84UZRxUI72QB_gZ766hl93dm4c318jc-ndccZQ"
pmTOKEN = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQxMTE4djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTc0Nzc5MzI2MywiaWQiOiIwMTkzNDRjMC0yNDdjLTdjMDEtOWY2MS1hMmViNjJiMmMwMWQiLCJpaWQiOjEyNTMwMzM5Nywib2lkIjo0MTY1MjYxLCJzIjoxMDQwLCJzaWQiOiJlNDJjZmQ5MS1kODNkLTRlNDMtYTQ0OS1iMjUxZWM0YjBkNWQiLCJ0IjpmYWxzZSwidWlkIjoxMjUzMDMzOTd9.Z9-JkdQR_Lynca2IvFPMK-d3fS-0ZE3Ks3uVGNBiwbRC27N-XuMphKQjMoRNE1QBizCybjEI01fWfgUlPG-eWw"


testHeaders = {'Authorization' : testTOKEN}
pmHeaders = {'Authorization' : pmTOKEN}
# jsonstr = {'name' : 'test'}
jsonlist = {'limit' : 10, 'next' : 0}
jsonid = {'supplyID' : 'WB-GI-120804005'}

info = requests.get("https://supplies-api.wildberries.ru/api/v1/acceptance/coefficients", headers=pmHeaders, params="warehouseIDs=120762")
# jsonstr = json.dumps(info.json(), indent=1)
# pr = json.loads(jsonstr)
for i in range(42):
    if info.json()[i]['boxTypeName'] == "Короба":
        print(info.json()[i])
        print()
