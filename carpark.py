# # import json
# # from urllib.request import urlopen


# # with urlopen("https://developers.data.gov.sg/data-gov-sg-apis/apis/get/transport/carpark-availability") as r:
# # 	source=r.read()

# # # data = json.loads(source) #step 1
# # # print(json.dumps(data, indent=4)) #step 2
# # print (source)

# # "https://api.data.gov.sg/v1/transport/carpark-availability" -H "accept: application/json"

# import urllib.parse
import requests
import json

r = requests.get("https://api.data.gov.sg/v1/transport/carpark-availability")
# print(r.json()
data = json.dumps(r.json(), indent=2)
# print(data)
print()
print()

data2=(r.json())
print ('what type(r.json()) ')
print(type(r.json())) #the response is a dict
print()
print()
print('what r the keys in r.json().keys() ? there is only 1 key')
print(r.json().keys())
print()
print()
print ('what type is items in r.json')
data3=data2['items'] #item is one of the keys of the dict
print(type(data3))
print()
print()
print ('what type is content of items in r.json')
print(data3[0].keys())
print()
print()
print ('what type is carpark data')
print(type(data3[0]['carpark_data'])) # this is a list
print ('how many items in carpark data list')
print(len(data3[0]['carpark_data'])) # the list has 1986 items
print()
print()
print ('print the first item, which is a dict')
print(data3[0]['carpark_data'][0])#print the first item, which is a dict
print ('print the keys of dict')
print(data3[0]['carpark_data'][0].keys()) #this dict has 3 keys
print ('print the value of key carpark number')
print(data3[0]['carpark_data'][0]['carpark_number']) # finally narrow down to carpark number of first list item
print()
print()
#Next to print out carpark number in one line
print ('the first carpark number in one line')
print(data2['items'][0]['carpark_data'][0]['carpark_number'])
print()
print()


#Next to print out all carpark number using a for loop
for item in data2['items'][0]['carpark_data']:
	if str(item['carpark_number']) == 'S100':
		print ("Carpark Number : "+str(item['carpark_number']))
		print ("Total lots = " + str(item['carpark_info'][0]['total_lots']))
		print()
