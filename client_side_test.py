'''
Created on Jun 22, 2014

@author: Dell
'''

import urllib2
import json
import os
from aquabrim_project.settings import BASE_DIR


debug_file = os.path.join(BASE_DIR, 'debug.html')

url = "http://localhost:8000/machine/send_data_to_server/"
#url = "http://162.251.84.104//machine/send_data_to_server/"

data = {'name':'washer', 'field_1': '1', 'field_2': '2', 'username':'nikaashpuri', 'password':'123456'}

data = json.dumps(data)

req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
f = urllib2.urlopen(req)
resp = f.read()
f.close()

f = open(debug_file, 'w+')
print resp
f.write(resp)
f.close()