import subprocess
import urllib.request

def try_fetch(ip):
    try:
        url = f"http://{ip}:8080/ph.zuscoffee.com_trends_syxbuqqh48_20260610T074007Z.json"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=1) as response:
            print(f"SUCCESS {ip}", response.read().decode()[:200])
    except Exception as e:
        # print(f"FAIL {ip}", e)
        pass

out = subprocess.run("ip route | awk '/default/ { print $3 }'", shell=True, capture_output=True, text=True)
gateway = out.stdout.strip()
print("Gateway:", gateway)

try_fetch("127.0.0.1")
try_fetch(gateway)
try_fetch("172.17.0.1")
