import requests

# Send a GET request to a public API
url = "https://api.github.com"
response = requests.get(url)

# Check the status code
print("Status code:", response.status_code)

# Display a part of the JSON response
data = response.json()
print("API information:", data.get("current_user_url"))
