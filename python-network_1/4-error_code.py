import request
import sys
url=sys[1]
res_1=request.get(url)
if res_1.status > 400:
    print("Error code:{}".format(res_1.status_code))
