from models.models import RequestsAmountModel, RequestsAmountByTypeModel, MostFrequentRequests, \
    BiggestRequestsWithRequestStatus4XX, TopUsersByAmountOfRequestsWithStatus5XX
from parsers.log_analyzer import LogAnalyzer


class MysqlBuilder:
    def __init__(self, client, analyzer: LogAnalyzer):
        self.client = client
        self.analyzer = analyzer

    def add_requests_amount(self, amount=None):
        data = self.analyzer.get_requests_count()
        requests_amount = RequestsAmountModel(
            amount=data
        )
        self.client.session.add(requests_amount)
        self.client.session.commit()

    def add_requests_amount_by_types(self, request_type=None, request_amount=None):
        data = self.analyzer.get_requests_count_by_type()
        for i in data:
            request_amount_by_type = RequestsAmountByTypeModel(
                requests_type=i[0],
                requests_amount=i[1],
            )
            self.client.session.add(request_amount_by_type)
        self.client.session.commit()

    def add_most_frequent_requests(self, top, request_url=None, request_amount=None):
        data = self.analyzer.get_top_requests(top)
        for i in data:
            most_frequent_requests = MostFrequentRequests(
                request_url=i[0],
                request_amount=i[1]
            )
            self.client.session.add(most_frequent_requests)
        self.client.session.commit()

    def add_biggest_requests_with_request_status_4XX(
            self,
            top,
            request_url=None,
            status_code=None,
            request_size=None,
            user_ip=None,
    ):  # :)
        data = self.analyzer.get_top_memory_4XX_error_requests(top)
        for i in data:
            biggest_requests_with_request_status_4XX = BiggestRequestsWithRequestStatus4XX(
                request_url=i[0],
                status_code=i[1],
                request_size=i[2],
                user_ip=i[3],
            )
            self.client.session.add(biggest_requests_with_request_status_4XX)
        self.client.session.commit()

    def add_top_users_by_amount_of_requests_with_status_5XX(self, top, user_ip=None, requests_amount=None):
        data = self.analyzer.get_top_users_5XX_error_requests(top)
        for i in data:
            top_users_by_amount_of_requests_with_status_5xx = TopUsersByAmountOfRequestsWithStatus5XX(
                user_ip=i[0],
                requests_amount=i[1],
            )
            self.client.session.add(top_users_by_amount_of_requests_with_status_5xx)
        self.client.session.commit()
