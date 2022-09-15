import json

import requests

url = 'https://reqres.in'
path_param = '/api/users'
query_param = 'page=2'

endpoint= url+path_param+'?'+query_param

res = requests.get(endpoint, verify=False)

status = res.status_code
# print(status)
# response = json.loads(res.text)
# print(type(response))

response = res.json()
print(res.headers)
print(res.status_code)
print(res.headers['Date'])

per_page = response['per_page']
print(per_page)


