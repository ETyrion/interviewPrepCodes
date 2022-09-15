import json

import requests

with open('reqBody.json') as f:
    req_bdy = json.load(f)
    print(req_bdy)
    req_bdy['name'] = 'Mohit'
    req_bdy['job'] = 'ML'

url = 'https://reqres.in/api/users'

res = requests.post(url, data=req_bdy, verify=False)
res_json = res.json()
print(res_json)
assert res.status_code == 201

print(res.headers['Date'])
