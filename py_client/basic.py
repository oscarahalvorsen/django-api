import requests

endpoint = "http://httpbin.org/anything"
 
get_response=requests.get(endpoint).text
print(get_response)