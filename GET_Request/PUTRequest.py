import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users/2"

# Read the payload
file = open('C:\\Users\\umair.anis\\API_Automation\\Create_User.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

# Make put request with JSON input payload
response = requests.put(url,request_json)

# Validating a response code
assert response.status_code == 200

#Fetch header from the response
response.headers.get('Content-Length')

# Parse response to Json format
response_json = json.loads(response.text)
print(response_json)

# Pick id using json path
#name = jsonpath.jsonpath(response_json,'name')
#print(name[0])

