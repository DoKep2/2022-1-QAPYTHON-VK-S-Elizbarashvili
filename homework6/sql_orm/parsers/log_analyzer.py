from parsers.methods import Methods


class LogAnalyzer:
    def __init__(self):
        self.methods = Methods()

    def get_requests_count_by_type(self):
        request_types = self.methods.get_request_types()
        res = []
        for request_type in request_types:
            res.append(self.methods.get_request_count_by_type(request_type))
        return res

    def get_requests_count(self):
        lines = self.methods.lines
        return len(lines)

    def get_top_requests(self, top):
        urls = self.methods.get_urls()
        urls_dict = {}
        for url in urls:
            urls_dict.update({url: urls_dict.get(url, 0) + 1})
        cnt = 0
        res = []
        for url in sorted(urls_dict, key=urls_dict.get, reverse=True):
            res.append((url, urls_dict.get(url)))
            cnt += 1
            if cnt == top:
                break
        return res

    def get_top_memory_4XX_error_requests(self, top):
        requests = sorted(self.methods.get_requests_by_request_status("4.."), key=lambda x: int(x.body_bytes_send),
                          reverse=True)
        cnt = 0
        res = []
        for i in requests:
            res.append((i.request_url, i.request_status, i.body_bytes_send, i.ip))
            cnt += 1
            if cnt == top:
                break
        return res

    def get_top_users_5XX_error_requests(self, top):
        requests = self.methods.get_requests_by_request_status("5..")
        requests_dict = {}
        for request in requests:
            requests_dict.update({request.ip: requests_dict.get(request.ip, 0) + 1})
        cnt = 0
        res = []
        for request in sorted(requests_dict, key=requests_dict.get, reverse=True):
            res.append((request, requests_dict.get(request)))
            cnt += 1
            if cnt == top:
                break
        return res