#!/usr/bin/python3 

import requests 

# URL we want to use for our API; 
BASE = "http://127.0.0.1:5000/"

my_data = [{"artist":"River Man", "song":"Rain", "streams":10000},
 {"artist":"Stick Man", "song":"Stick Song", "streams":1000},
{"artist":"Water", "song":"Dried Up", "streams":17000},
 {"artist":"Trains and Cars", "song":"First Time On A Plane", "streams":10000}]

# iterate and create a new response
# throw in a dictionary object 
for tt in range(len(my_data)):
    response = requests.post(BASE + "playlist/" + str(tt), my_data[tt])
    print(response.json())




