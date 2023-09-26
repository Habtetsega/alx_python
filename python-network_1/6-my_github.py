import requests
import sys

# Get username and password from command line arguments
username = sys.argv[1]
password = sys.argv[2]

# Send GET request to GitHub API to get user information
response = requests.get("https://api.github.com/user", auth=(username, password))

# Check if the response is successful (status code 200)
if response.status_code == 200:
    # Display user id from the response
    json_data = response.json()
    print(json_data['id'])
else:
    print("Failed to retrieve user information")

