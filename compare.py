import urllib.request
import json
import sys

url1 = "http://localhost:8080/ph.zuscoffee.com_trends_syxbuqqh48_20260610T074007Z.json"
url2 = "http://localhost:8080/ph.zuscoffee.com.mirror_trends_vipskliivd_20260610T073930Z.json"

def fetch_json(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def main():
    try:
        legacy = fetch_json(url1)
        mirror = fetch_json(url2)
        
        print("=== LEGACY DATA ===")
        print(json.dumps(legacy, indent=2))
        
        print("\n=== MIRROR DATA ===")
        print(json.dumps(mirror, indent=2))
        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
