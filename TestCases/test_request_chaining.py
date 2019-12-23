import requests
import jsonpath
import json


def test_Add_New_Data():
    global id
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Users\\umair.anis\\API_Automation\\AddStudent.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL,json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

def test_get_details():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/"+ str(id[0])
    response = requests.get(API_URL)
    print(response.text)