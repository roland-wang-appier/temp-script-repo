import urllib.request
try:
    req = urllib.request.Request("http://host.docker.internal:8080/ph.zuscoffee.com_trends_syxbuqqh48_20260610T074007Z.json")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode()[:500])
except Exception as e:
    print(e)
