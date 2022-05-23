import json
import threading

from flask import Flask, jsonify, request

from homework7 import settings

app = Flask(__name__)

RATE_DATA = {}


@app.route('/get_teacher_rate/<name>', methods=['GET'])
def get_teacher_rate(name):
    if rate := RATE_DATA.get(name):
        return jsonify(rate), 200
    else:
        return jsonify(f'Rate for teacher {name} not found'), 404


@app.route('/add_rate', methods=['POST'])
def add_teacher_rate():
    teacher_name = json.loads(request.data)['name']
    teacher_rate = json.loads(request.data)['rate']
    if teacher_name not in RATE_DATA:
        RATE_DATA[teacher_name] = teacher_rate
        data = {teacher_name: teacher_rate}
        return jsonify(data), 201
    else:
        return jsonify(f'Teacher rate {teacher_name} already exists', 400)


@app.route('/update_rate/<teacher_name>', methods=['PUT'])
def update_teacher_rate(teacher_name):
    teacher_rate = json.loads(request.data)['rate']
    if teacher_name in RATE_DATA:
        RATE_DATA[teacher_name] = teacher_rate
        data = {teacher_name: teacher_rate}
        return jsonify(data), 201
    else:
        return jsonify(f'Teacher {teacher_name} not found'), 404


@app.route('/delete_rate/<teacher_name>', methods=['DELETE'])
def delete_teacher_rate(teacher_name):
    if teacher_name in RATE_DATA:
        rate = RATE_DATA.pop(teacher_name)
        data = {teacher_name: rate}
        return jsonify(data), 204
    else:
        return jsonify(f'Teacher {teacher_name} not found'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200
