from flask import Flask, jsonify, request

app = Flask(__name__)

plants = []
tasks = []

class Plant:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

class Task:
    def __init__(self, title, description, done):
        self.title = title
        self.description = description
        self.done = done

@app.route("/")
def root():
    return jsonify({"message": "Hello World"})

@app.route("/plants", methods=["POST"])
def create_plant():
    data = request.get_json()
    plant = Plant(data['name'], data['type'], data['age'])
    plants.append(plant.__dict__)
    return jsonify(plant.__dict__)

@app.route("/plants")
def read_plants():
    return jsonify(plants)

@app.route("/plants/<int:plant_id>")
def read_plant(plant_id):
    return jsonify(plants[plant_id])

@app.route("/plants/<int:plant_id>", methods=["PUT"])
def update_plant(plant_id):
    data = request.get_json()
    plant = Plant(data['name'], data['type'], data['age'])
    plants[plant_id] = plant.__dict__
    return jsonify(plant.__dict__)

@app.route("/plants/<int:plant_id>", methods=["DELETE"])
def delete_plant(plant_id):
    plants.pop(plant_id)
    return jsonify({"message": "Plant deleted"})

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = Task(data['title'], data['description'], data['done'])
    tasks.append(task.__dict__)
    return jsonify(task.__dict__)

@app.route("/tasks")
def read_tasks():
    return jsonify(tasks)

@app.route("/tasks/<int:task_id>")
def read_task(task_id):
    return jsonify(tasks[task_id])

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    task = Task(data['title'], data['description'], data['done'])
    tasks[task_id] = task.__dict__
    return jsonify(task.__dict__)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks.pop(task_id)
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)