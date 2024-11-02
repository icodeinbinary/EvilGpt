import requests

url = "https://white-evilgpt.ashlynn.workers.dev/"
params = {
    "question": "how are you",
    "state": "evilgpt"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Response message:", data["message"])
else:
    print("Failed to retrieve data. Status code:", response.status_code)
