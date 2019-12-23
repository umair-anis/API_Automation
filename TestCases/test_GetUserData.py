import requests
import json
import jsonpath
import pytest

@pytest.mark.Smoke
def test_fetch_user_details():
    # API URL
    url = "https://reqres.in/api/users?page=2"
    # Send Get Request
    response=requests.get(url)
    # Parse response to json format
    json_response = json.loads(response.text)
    for i in range(0, 3):
        firstName = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
        print(firstName[0])
