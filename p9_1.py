import urllib.request
import requests

opener = urllib.request.build_opener()
response = opener.open("http://httpbin.org/get")
print(response.read())

response = requests.get("http://httpbin.org/get")
print(response.text)
