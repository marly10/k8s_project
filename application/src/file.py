import requests

new_plant = {"name": "Rose", "type": "Flower", "age": 2}
response = requests.post("http://127.0.0.1:5000/plants", json=new_plant)
print(response.json())  # prints the created plant object
