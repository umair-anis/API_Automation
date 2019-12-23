import requests
import jsonpath
import json


def test_Add_New_Data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Users\\umair.anis\\API_Automation\\RequestJson.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(API_URL,request_json)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    Tech_API_URL = "http://thetestingworldapi.com/api/technicalskills"
    f = open('C:\\Users\\umair.anis\\API_Automation\\TechDetails.json', 'r')
    request_json = json.loads(f.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(Tech_API_URL,request_json)
    print(response.text)


    address_API_URL = "http://thetestingworldapi.com/api/addresses"
    f = open('C:\\Users\\umair.anis\\API_Automation\\address.json', 'r')
    request_json = json.loads(f.read())
    request_json['st_id']=id[0]
    response = requests.post(address_API_URL,request_json)
    print(response.text)


    final_details_API_URL = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details_API_URL)
    print(response.text)

