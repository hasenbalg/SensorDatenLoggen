
import requests, collections

url = 'http://192.168.9.121/api/E4892536FE/sensors'
resp = requests.get(url=url)
data = resp.json() # Check the JSON Response Content documentation below

sensorNames =['Schlafzimmersensor', 'Badsensor', 'Kuechensensor', 'Wohnzimmersensor']

datasets = {}
for sensor in data:
    name = data[sensor]['name']

    if name in sensorNames:
        if name not in datasets:
            datasets[name] = {}
        if 'lastupdated' not in datasets[name] or datasets[name]['lastupdated'] < data[sensor]['state']['lastupdated']:
            datasets[name]['lastupdated'] = data[sensor]['state']['lastupdated']
        
        if 'temperature' in data[sensor]['state']:
            datasets[name]['temperature'] = data[sensor]['state']['temperature'] / 100
        if 'pressure' in data[sensor]['state']:
            datasets[name]['pressure'] = data[sensor]['state']['pressure']
        if 'humidity' in data[sensor]['state']:
            datasets[name]['humidity'] = data[sensor]['state']['humidity']
        if 'battery' in data[sensor]['config'] and data[sensor]['config']['battery'] is not None:
            datasets[name]['battery'] = data[sensor]['config']['battery']



for key in datasets:
    datasets[key] = collections.OrderedDict(sorted(datasets[key].items()))  
    newLine = ','.join(map(str, list(datasets[key].values())))
    allLines = []
    try:
        with open(key + '.csv') as csvfile:
            allLines = csvfile.read().splitlines()
    except:
        pass
    finally:
        allLines.append(newLine)
        valuesList = []
        for line in allLines:
            valueSet = line.split(',')
            if valueSet not in valuesList:
                valuesList.append(valueSet)
        valuesList.sort(key=lambda x:x[2])
        #valuesList = set(valuesList)
        with open(key + '.csv', 'w') as csvfile:
            for valueSet in valuesList:
                csvfile.write(",".join(valueSet) + '\n')


    
