import requests
import sys

# Get letter from command line argument
if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

# Send POST request to http://0.0.0.0:5000/search_user with letter as a parameter
response = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})

# Check if the response body is properly JSON formatted and not empty
try:
    json_data = response.json()
    if json_data:
        # Display id and name from the JSON response
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
