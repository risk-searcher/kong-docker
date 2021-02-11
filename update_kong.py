#!/usr/bin/env python3
import requests
import json
import time

url = 'http://localhost:8001'
r = requests.get(url = url, verify=False) 
print("Kong version: " + r.json()['version'])

r = requests.get(url = url + '/routes', verify=False) 
j =  r.json()
for i in range(len(j['data'])):
    route = j['data'][i]
    print("[" +  str(i+1) + "] route: " + route['id'] + " " + route['name'])

n = input("Enter the route number : ") 
n = int(n) - 1
route_id = j['data'][n]['id']
route_name = j['data'][n]['name']
r = requests.get(url = url + '/routes/' + route_id + '/plugins', verify=False) 
j = r.json()
for i in range(len(j['data'])):
    plugin = j['data'][i]
    print('[' + str(i+1) + '] plugin: ' + plugin['id'] + ' ' + plugin['name'])

print('[' + str(len(j['data'])+1) + '] add new plugin')

n = input("Enter the plugin you want to update: ")
n = int(n) - 1
filename =  input("Enter the new plugin config file: ")
file_content = ""
with open(filename, 'r') as myfile:
  file_content = myfile.read()

if len(j['data']) > n:
    plugin_config = json.loads(file_content)
    r = requests.get(url = url + '/plugins/' + j['data'][n]['id'], verify=False) 
    ts = int(time.time())
    with open(f"./backup/{route_name}-{plugin_config['name']}-{ts}.json", 'w') as backup:
        backup.write(r.text)
    if j['data'][n]['name'] != plugin_config['name']:
        print('Plugin config: ' + plugin_config['name'] + " != " + j['data'][n]['name'])
    print("Delete plugin...")
    r = requests.delete(url = url + '/plugins/' + j['data'][n]['id'], verify=False) 

print("Add new plugin...")
headers = {'Content-type': 'application/json'}
r = requests.post(url = url + '/routes/' + route_id + '/plugins', headers = headers, data = file_content, verify=False)
print(r.json()) 
print("HTTP " + str(r.status_code) + " " + r.reason + ": plugin_id=" + r.json()['id'])
