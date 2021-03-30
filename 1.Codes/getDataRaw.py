import json

with open('zeusDataRaw.json','r') as f:
    items = json.load(f)
    for item in items:
        try:
            print(item['data.data_raw'])
        except KeyError:
            print('noData') 
