import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get('https://api.github.com/user',auth=HTTPBasicAuth('anisum@hotmail.com','Orange@12_6'))
    print(response.text)