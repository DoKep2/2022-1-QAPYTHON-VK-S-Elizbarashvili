import threading

from flask import Flask, jsonify, request

from settings import MOCK_HOST, MOCK_PORT

app = Flask(__name__)

VK_ID_DATA = {
    "DoKepDoKep": "123"
}


@app.route('/vk_id/<username>', methods=['GET'])
def get_vk_id(username):
    if vk_id := VK_ID_DATA.get(username):
        return {'vk_id': vk_id}, 200
    else:
        return jsonify({}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': MOCK_HOST,
        'port': MOCK_PORT
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
