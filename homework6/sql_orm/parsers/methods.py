import os
import re


class Methods:
    def __init__(self):
        from conftest import repo_root
        self.lines = self.get_requests_lines(repo_root())

    @staticmethod
    def get_requests_lines(repo_root):
        root_path = repo_root
        with open(f'{root_path}{os.sep}access.log') as file:
            lines = file.readlines()
        from parsers.log_components.request_line import RequestLine
        requests_lines = [RequestLine(*i.split(' ')) for i in lines]

        return requests_lines

    def get_urls(self):
        urls = [line.request_url for line in self.lines]
        return urls

    def get_request_count_by_type(self, request_type):
        res = 0
        for i in self.lines:
            if request_type in i.request_type:
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
            types.add(i.request_type[1:])
        return types
