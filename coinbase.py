import requests
import json

print('Just a Basic API call using Requests and Json Lib')
print()

r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# data=json.dumps(r)
print('##### This r.text and r.content look like raw format cannot do indexing')
print()
print(r.text) # i think this cannot do indexing
print()
print('##### This r.json() format shld alway be used, similar to json.loads')
print()

print(r.json()) # this is shortcut to json format, equal to print(json.loads(r.text))
print()
print ('######## To extract BTC price using  r.json() bpi - usd - rate ''######')
print ("BTC price is $" + r.json()['bpi']['USD']['rate']) # this is dict indexing using the json
print()
print()
print('##### This json.dumps(r.json(), indent=2)) is to indent the json format. We get dict inside a dict')
print()
print()
data = json.dumps(r.json(), indent=2)
print(data)
print(type(r.json()))
