import requests
import sys

# Get URL and email address from command line arguments
url = sys.argv[1]
email = sys.argv[2]

# Send POST request to the URL with email as a parameter
response = requests.post(url, data={'email': email})

# Display the body of the response
print(response.text)
