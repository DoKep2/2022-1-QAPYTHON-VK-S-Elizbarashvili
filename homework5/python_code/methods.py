import re

from log_components.request_line import RequestLine


class Methods:
    def __init__(self):
        self.lines = self.get_requests_lines()

    @staticmethod
    def get_requests_lines():
        with open('access.log') as file:
            lines = file.readlines()
        requests_lines = [RequestLine(*i.split(' ')) for i in lines]
        gen_delims = ['?', "#"]
        for line in requests_lines:
            line.request_type = line.request_type[1:]
            for delim in gen_delims:
                if delim in line.request_url:
                    line.request_url = line.request_url.split(delim)[0]
        return requests_lines

    def get_urls(self):
        urls = [line.request_url for line in self.lines]
        return urls

    def get_request_count_by_type(self, request_type):
        res = 0
        for i in self.lines:
            if request_type == i.request_type:
                res += 1
        return request_type, res

    def get_requests_by_request_status(self, status_pattern):
        res = []
        for i in self.lines:
            if re.search(status_pattern, i.request_status):
                res.append(i)
        return res

    def get_request_types(self):
        types = set()
        for i in self.lines:
            types.add(i.request_type)
        return types
