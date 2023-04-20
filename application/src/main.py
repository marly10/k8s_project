from flask import Flask, jsonify, request, render_template

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
    return render_template('home.html')


@app.route("/plants", methods=["POST"])
def create_plant():
    name = request.form['name']
    plant_type = request.form['type']
    age = request.form['age']
    plant = Plant(name, plant_type, age)
    plants.append(plant.__dict__)
    return render_template('plants.html', plants=plants)


@app.route("/plants")
def read_plants():
    return render_template('plants.html', plants=plants)


@app.route("/plants/<int:plant_id>")
def read_plant(plant_id):
    return render_template('plant.html', plant=plants[plant_id])


@app.route("/plants/<int:plant_id>/edit", methods=["GET", "POST"])
def update_plant(plant_id):
    if request.method == "POST":
        name = request.form['name']
        plant_type = request.form['type']
        age = request.form['age']
        plant = Plant(name, plant_type, age)
        plants[plant_id] = plant.__dict__
        return render_template('plants.html', plants=plants)
    else:
        return render_template('edit_plant.html', plant=plants[plant_id])


@app.route("/plants/<int:plant_id>/delete", methods=["POST"])
def delete_plant(plant_id):
    plants.pop(plant_id)
    return render_template('plants.html', plants=plants)


@app.route("/tasks", methods=["POST"])
def create_task():
    title = request.form['title']
    description = request.form['description']
    done = request.form['done']
    task = Task(title, description, done)
    tasks.append(task.__dict__)
    return render_template('tasks.html', tasks=tasks)


@app.route("/tasks")
def read_tasks():
    return render_template('tasks.html', tasks=tasks)


@app.route("/tasks/<int:task_id>")
def read_task(task_id):
    return render_template('task.html', task=tasks[task_id])


@app.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
def update_task(task_id):
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        done = request.form['done']
        task = Task(title, description, done)
        tasks[task_id] = task.__dict__
        return render_template('tasks.html', tasks=tasks)
    else:
        return render_template('edit_task.html', task=tasks[task_id])


@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    tasks.pop(task_id)
    return render_template('tasks.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)
