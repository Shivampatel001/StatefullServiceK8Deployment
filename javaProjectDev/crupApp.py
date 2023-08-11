import requests

url = 'http://192.168.49.2:30565/orders'
data = {
    "name": "Shivam",
    "qty": 50,
    "price": 999
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("POST request successful. Order created.")
else:
    print(f"POST request failed with status code: {response.status_code}")

