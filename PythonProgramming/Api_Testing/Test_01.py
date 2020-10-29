import requests

res = requests.get("https://www.google.co.in/")
print(res)
print(res.cookies)
print(res.url)
print(res.text)
print(res.status_code)