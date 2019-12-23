import requests
import jsonpath
import json


def test_o_authentication():

    token_url = "http://thetestingworldapi.com/Token"
    data = {'grant_type':'password','username':'admin','password':'adminpass'}
    response = requests.post(token_url,data)
    token_value = jsonpath.jsonpath(response.json(),'access_token')
    print(response.text)

    auth={'Authorization':'Bearer '+token_value[0]}
    API_URL = "http://thetestingworldapi.com/api/StDetails/1104"
    response = requests.get(API_URL,headers=auth)
    print(response.text)
