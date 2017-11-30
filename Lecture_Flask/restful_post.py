from flask import Flask, jsonify, render_template
app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

# choose one of task
from flask import abort
@app.route('/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [tTemp for tTemp in tasks if tTemp['id'] == task_id]
#     task = list()
#     for tTemp in tasks:
#         if tTemp['id'] == task_id:
#             task.append(tTemp)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# 404 error handler
from flask import make_response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

from flask import request

@app.route('/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

from flask import url_for

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/api/v1.0/tasks/external', methods=['GET'])
def get_externaltasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

@app.route('/restful_post', methods = ['GET', 'POST'])
def restful_get():
    return render_template('restful_post.html')

if __name__ == '__main__':
    app.run(debug=True)