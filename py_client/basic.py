import requests

endpoint = "http://localhost:8000/"

get_response=requests.get(endpoint).text
print(get_response)