import requests
import sys
user=sys.argv[1]
pwd=sys.argv[2]
res=requests.git("https://api.github.com/user",auth=(user,pwd))
if res.status_code == 200:
    json_data = res.json
    print(json_data['id'])
else:
    print("failed")
