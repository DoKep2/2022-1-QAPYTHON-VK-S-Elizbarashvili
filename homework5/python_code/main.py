from methods import *


class LogAnalyzer:
    def __init__(self, file):
        self.methods = Methods()
        self.file = file

    def write(self, *text):
        self.file.write(str(text) + "\n")

    def print_request_count_by_type(self):
        request_types = self.methods.get_request_types()
        for request_type in request_types:
            self.write(self.methods.get_request_count_by_type(request_type))

    def print_request_count(self):
        lines = self.methods.lines
        self.write(len(lines))

    def print_top_requests(self, top):
        urls = self.methods.get_urls()
        urls_dict = {}
        for url in urls:
            urls_dict.update({url: urls_dict.get(url, 0) + 1})
        cnt = 0
        for url in sorted(urls_dict, key=urls_dict.get, reverse=True):
            self.write(url, urls_dict.get(url))
            cnt += 1
            if cnt == top:
                break

    def print_top_memory_4XX_error_requests(self, top):
        requests = sorted(self.methods.get_requests_by_request_status("4.."), key=lambda x: int(x.body_bytes_send),
                          reverse=True)
        cnt = 0
        for i in requests:
            self.write(i.request_url, i.request_status, i.body_bytes_send, i.ip)
            cnt += 1
            if cnt == top:
                break

    def print_top_users_5XX_error_requests(self, top):
        requests = self.methods.get_requests_by_request_status("5..")
        requests_dict = {}
        for request in requests:
            requests_dict.update({request.ip: requests_dict.get(request.ip, 0) + 1})
        cnt = 0
        for request in sorted(requests_dict, key=requests_dict.get, reverse=True):
            self.write(request, requests_dict.get(request))
            cnt += 1
            if cnt == top:
                break


file = open("result.txt", "w")

log_analyzer = LogAnalyzer(file)
file.write("----------Requests amount:----------\n")

log_analyzer.print_request_count()
file.write("----------Requests amount by type (type, amount):----------\n")

log_analyzer.print_request_count_by_type()
file.write("----------10 the most frequent requests (url, amount):----------\n")

log_analyzer.print_top_requests(10)
file.write("----------5 the biggest requests with request status 4XX (url, status code, size, ip):----------\n")

log_analyzer.print_top_memory_4XX_error_requests(5)
file.write("----------Top-5 users by amount of requests with status 5XX (ip, amount):----------\n")

log_analyzer.print_top_users_5XX_error_requests(5)
file.close()
