import requests

new_plant = {"name": "Rose", "type": "Flower", "age": 2}
response = requests.post("http://localhost:8000/plants", json=new_plant)
print(response.json())  # prints the created plant object
