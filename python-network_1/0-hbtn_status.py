import requests

def fetch_status():
    """
    Fetches https://alu-intranet.hbtn.io/status using the requests package.

    Returns:
        str: The body response content.
    """
    # Send a GET request to the URL
    response = requests.get("https://alu-intranet.hbtn.io/status")

    # Return the body response content
    return response.text

# Print the body response with the required format
body_response = fetch_status()
print("Body response:")
print("\t- type: {}".format(type(body_response)))
print("\t- content: {}".format(body_response))
