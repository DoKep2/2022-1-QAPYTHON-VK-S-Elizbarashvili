

from parsers.log_components.local_time import LocalTime


class RequestLine:
    def __init__(self, ip, remote_addr, remote_user, date, GMT, request_type, request_url, protocol, request_status,
                 body_bytes_send, http_referer, *http_user_agent):
        self.ip = ip
        self.remote_addr = remote_addr
        self.remote_user = remote_user
        self.time_local = LocalTime(date, GMT)
        self.protocol = protocol
        self.request_type = request_type
        self.request_url = request_url
        self.request_status = request_status
        self.body_bytes_send = body_bytes_send
        self.http_referer = http_referer
        self.http_user_agent = http_user_agent
