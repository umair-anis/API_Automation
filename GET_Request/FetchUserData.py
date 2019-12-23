import requests
import json
import jsonpath

# API URIL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response=requests.get(url)
#print(response)

# Display response content
#print(response.content)
#print(response.headers)


# Validate status code
#print(response.status_code)

#assert response.status_code == 200

# Fetch response header
#print(response.headers)
#print(response.headers.get('Date'))
#print(response.headers.get('Server'))

# Fetch Cookies
#print(response.cookies)

#Fetch encoding
#print(response.encoding)

# Fetch Elapsed time
#print(response.elapsed)


# Parse response to json format

json_response = json.loads(response.text)
#print(json_response)

#pages = jsonpath.jsonpath(json_response,'total_pages')
#assert (pages[0]) == 2

for i in range (0,3):
    firstName = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(firstName[0])











