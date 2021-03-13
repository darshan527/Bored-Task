import requests

url = "http://www.boredapi.com/api/activity/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
