import requests

param={'user_name':'umair','password':'abc_123','phone_number':'952-120-2345'}
response=requests.get('https://httpbin.org/get', params=param)
print(response.text)