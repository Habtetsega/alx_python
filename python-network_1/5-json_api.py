import requests
import sys
if len(sys.argv) > 1:
    char=sys.argv[1]
else:
    char=""
res = requests.post('http://0.0.0.0:5000/search_user',data={'q':char})
try :
    json_data=res.json
    if json_data:
        print("[{}] {}".format(json.data["id"], json.data["name"]))
    else :
        print("No result")
except ValueError:
    print("Not a valid JSON")
