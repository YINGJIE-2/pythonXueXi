import requests
data={
    "kw":"周杰伦"
}
r=requests.get("https://www.baidu.com",params=data)
print(r.url)