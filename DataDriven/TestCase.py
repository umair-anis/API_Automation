import openpyxl
import requests
import jsonpath
import json
import lxml.html

from DataDriven import Library

def test_Add_Multiple_Students():
    # API
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Users\\umair.anis\\API_Automation\\AddStudent.json')
    json_request = json.loads(f.read())

    obj = Library.Common("C:\\Users\\umair.anis\\API_Automation\\multiple_students.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_name()

    for i in range(2, row + 1):
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(API_URL, updated_json_request)
        print(response)
        assert response.status_code == 201