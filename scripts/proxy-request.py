import requests

proxies = {"http": "http://145.239.85.58" }

r = requests.get("https://ipinfo.io/json", proxies=proxies)

print(r.content)
