import requests
import json
import jsonpath
import pytest


# API URL
url = "https://reqres.in/api/users"

#@pytest.mark.skip("This is not valid for current build")
@pytest.fixture
def start_exec():
    global file
    file = open('C:\\Users\\umair.anis\\API_Automation\\Create_User.json', 'r')

@pytest.mark.Smoke
def test_create_new_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
   # Make post request with JSON input payload
    response = requests.post(url,request_json)
    # Validating a response code
    assert response.status_code == 201
    #Fetch header from the response
    #response.headers.get('Content-Length')
    # Parse response to Json format
    #response_json = json.loads(response.text)
    # Pick id using json path
    #id = jsonpath.jsonpath(response_json,'id')
    #print(id[0])

@pytest.mark.Sanity
def test_create_other_user(start_exec):

    json_input = file.read()
    request_json = json.loads(json_input)
    #print(request_json)
   # Make post request with JSON input payload
    response = requests.post(url,request_json)
    # Validating a response code
    #assert response.status_code == 202
    #Fetch header from the response
    #response.headers.get('Content-Length')
    # Parse response to Json format
    response_json = json.loads(response.text)
    # Pick id using json path
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])
