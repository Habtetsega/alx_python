import requests
import sys

def get_request_id(url):
    """
    Sends a request to the specified URL and returns the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str or None: The value of the X-Request-Id header or None if the header is not found.
    """
    # Send a GET request to the URL
    response = requests.get(url)

    # Get the value of the X-Request-Id header
    request_id = response.headers.get('X-Request-Id')

    return request_id

# Get the URL from the command-line argument
url = sys.argv[1]

# Get the X-Request-Id and display it
request_id = get_request_id(url)
