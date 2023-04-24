from flask import Flask, jsonify, request, render_template
import logging
from flask_log_request_id import RequestID, current_request_id
from elasticsearch import Elasticsearch

app = Flask(__name__)
RequestID(app)

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

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

# Log section ELK stack:
    # ElasticSearch
    # Logstash
    # Kibana
def log_request_info():
    logger.info('Request ID: %s', current_request_id())
    logger.info('Request path: %s', request.path)
    logger.info('Request method: %s', request.method)
    logger.info('Request data: %s', request.get_data())
    
@app.route("/")
def root():
    log_request_info()
    return render_template('home.html')

@app.route("/plants", methods=["POST"])
def create_plant():
    log_request_info()
    name = request.form['name']
    plant_type = request.form['type']
    age = request.form['age']
    plant = Plant(name, plant_type, age)
    plants.append(plant.__dict__)
    return render_template('plants.html', plants=plants)

@app.route("/plants")
def read_plants():
    log_request_info()
    return render_template('plants.html', plants=plants)

@app.route("/plants/<int:plant_id>")
def read_plant(plant_id):
    log_request_info()
    return render_template('plant.html', plant=plants[plant_id])

@app.route("/plants/<int:plant_id>/edit", methods=["GET", "POST"])
def update_plant(plant_id):
    log_request_info()
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
    log_request_info()
    plants.pop(plant_id)
    return render_template('plants.html', plants=plants)

@app.route("/tasks", methods=["POST"])
def create_task():
    log_request_info()
    title = request.form['title']
    description = request.form['description']
    done = request.form['done']
    task = Task(title, description, done)
    tasks.append(task.__dict__)
    return render_template('tasks.html', tasks=tasks)


@app.route("/tasks")
def read_tasks():
    log_request_info()
    return render_template('tasks.html', tasks=tasks)

@app.route("/tasks/<int:task_id>")
def read_task(task_id):
    log_request_info()
    return render_template('task.html', task=tasks[task_id])

@app.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
def update_task(task_id):
    log_request_info()
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
    log_request_info()
    tasks.pop(task_id)
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
