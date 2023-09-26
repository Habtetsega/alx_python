import requests
import sys
url=sys.argv[1]
res_1=requests.get(url)
if res_1.status_code > 400:
    print("Error code:{}".format(res_1.status_code))
