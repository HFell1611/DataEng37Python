import requests
import json
from pprint import pprint


# pc_req = requests.get("https://api.postcodes.io/postcodes/CB8 9UP")

# print(pc_req, type(pc_req))
#
# if pc_req.status_code == 200:
#     # pprint(dict(pc_req.headers), sort_dicts=False)
#     print(pc_req.content, type(pc_req.content))
#     # postcode = json.loads(pc_req.content)
#     # print(postcode)
#     # print(postcode['result']['postcode'])
#     # print(pc_req.content['result']['postcode'])
#     postcode = pc_req.json()
#     print(type(postcode))
#
# # print the admin_district, the eating and northings, nuts code
#     pprint(postcode, sort_dicts=False)
#     print(postcode['result']['admin_district'])
#     print(postcode['result']['eastings'])
#     print(postcode['result']['northings'])
#     print(postcode['result']['codes']['nuts'])

body = {'postcodes': ['CW11 3RT', 'CB8 9UP', 'LE2 7JN']}
headers = {'Content-Type': 'application/json'}

pc_req = requests.post(
    "https://api.postcodes.io/postcodes/",
    headers=headers,
    data=json.dumps(body)
)

print(pc_req)
pcs = pc_req.json()['result']
# pprint(pcs, sort_dicts=False)

# admin_ward, eastings, northings, nuts code

# for i in pcs:
#     print(pcs['result']['admin_district'])
#     print(pcs['result']['eastings'])
#     print(pcs['result']['northings'])
#     print(pcs['result']['codes']['nuts'])

if pc_req.status_code == 200:
    for pc_data in pcs:
        result = pc_data['result']
        print('----', result['admin_ward'], '----')
        print(result['eastings'], result['northings'])
        print(result['codes']['nuts'])

