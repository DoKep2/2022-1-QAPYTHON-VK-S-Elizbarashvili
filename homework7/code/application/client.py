import json
import socket


class HttpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = None

    def close(self):
        self.client.close()

    def connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        client.connect((self.host, self.port))
        self.client = client

    def send_request(self, request_type, route, host, data=None):
        self.connect()
        request = f'{request_type} {route} HTTP/1.1\r\nHOST:{host}\r\n'
        if data is not None:
            request += f'Content-Type: application/json\r\nContent-Length:{str(len(data))}\r\n\r\n{data}'
        else:
            request += '\r\n'
        self.client.send(request.encode())
        response = self.client_recv()
        self.close()
        return response

    def get_teacher_rate(self, name):
        params = f'/get_teacher_rate/{name}'
        response = self.send_request(request_type="GET", route=params, host=self.host)
        return json.loads(response[-1])

    def add_teacher_rate(self, name, rate):
        data = json.dumps({"name": name,
                           "rate": rate})
        route = '/add_rate'
        request_type = 'POST'
        resp = self.send_request(request_type, route, host=self.host, data=data)
        return json.loads(resp[-1])

    def delete_teacher_rate(self, name):
        data = json.dumps({"name": name})
        route = f'/delete_rate/{name}'
        request_type = 'DELETE'
        self.send_request(request_type, route, host=self.host, data=data)

    def update_teacher_rate(self, name, new_rate):
        data = json.dumps({
            "name": name,
            "rate": new_rate,
        })
        route = f'/update_rate/{name}'
        request_type = 'PUT'
        resp = self.send_request(request_type, route, host=self.host, data=data)
        return json.loads(resp[-1])

    def client_recv(self):
        total_data = []
        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                self.client.close()
                break
        data = ''.join(total_data).splitlines()
        return data
