import requests

# from google.oauth2 import service_account
# from google.auth.transport.requests import Request

url = "https://collectionapi.metmuseum.org/public/collection/v1.1/search"

my_data = {
    'q': "Roses"
}
response = requests.get(url, data=my_data)
data = response.json()
print(data)