import requests
import jsonpath
import json


def test_add_student_data():

    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Users\\umair.anis\\API_Automation\\RequestJson.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

def test_update_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/150981"
    f = open('C:\\Users\\umair.anis\\API_Automation\\RequestJson.json', 'r')
    json_request = json.loads(f.read())
    response = requests.put(API_URL,json_request)
    print(response.text)


def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/150981"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    print(json_response)
    id = jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 150981

def test_delete_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/150981"
    response = requests.delete(API_URL)
    print(response.text)


def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/150981"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    print(json_response)
    id = jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 150981



