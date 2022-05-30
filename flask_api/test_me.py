#!/usr/bin/python3 

import requests 

# URL we want to use for our API; 
BASE = "http://127.0.0.1:5000/"

my_data = [{"Artist":"River Man", "Song":"Rain", "Streams":10000}, {"Artist":"Stick Man", "Song":"Stick Song", "Streams":1000},
{"Artist":"Water", "Song":"Dried Up", "Streams":17000}, {"Artist":"Trains and Cars", "Song":"First Time On A Plane", "Streams":10000}]

# this is the URL we want to retrieve
# response = requests.get(BASE + "doesthiswork/May")

# iterate and create a new response
# throw in a dictionary object 
for tt in range(len(my_data)):
    response = requests.post(BASE + "playlist/" + str(tt), my_data[tt])

response0 = requests.get(BASE + "playlist/0")

print(response0.json())


