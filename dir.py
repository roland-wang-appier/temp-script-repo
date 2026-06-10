import urllib.request
try:
    req = urllib.request.Request("http://localhost:8080/")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
except Exception as e:
    print(e)
