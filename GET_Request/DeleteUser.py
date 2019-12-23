import requests

# API URL
url = "https://reqres.in/api/users/2"

response = requests.delete(url)
print(response)

assert response.status_code == 204