import requests

url = "http://www.boredapi.com/api/activity/"

payload={
    'key' : '5881028'
}
headers = {}

response = requests.get(url,params=payload)

print(response.text)
