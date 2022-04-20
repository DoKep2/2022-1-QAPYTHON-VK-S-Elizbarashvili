import pytest

from mysql.client import MysqlClient
from utils.builder import MysqlBuilder
from models.models import RequestsAmountModel, RequestsAmountByTypeModel, MostFrequentRequests, \
    BiggestRequestsWithRequestStatus4XX, TopUsersByAmountOfRequestsWithStatus5XX


class MyTest:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client, log_analyzer):
        self.mysql: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.mysql, log_analyzer)

    def get_from_requests_amount(self, **filters):
        self.mysql.session.commit()
        res = self.mysql.session.query(RequestsAmountModel).filter_by(**filters)
        return res.all()

    def get_from_requests_amount_by_type(self, **filters):
        self.mysql.session.commit()
        res = self.mysql.session.query(RequestsAmountByTypeModel).filter_by(**filters)
        return res.all()

    def get_from_most_frequent_requests(self, **filters):
        self.mysql.session.commit()
        res = self.mysql.session.query(MostFrequentRequests).filter_by(**filters)
        return res.all()

    def get_from_biggest_requests_with_request_status_4XX(self, **filters):
        self.mysql.session.commit()
        res = self.mysql.session.query(BiggestRequestsWithRequestStatus4XX).filter_by(**filters)
        return res.all()

    def get_from_top_users_by_amount_of_requests_with_status_5XX(self, **filters):
        self.mysql.session.commit()
        res = self.mysql.session.query(TopUsersByAmountOfRequestsWithStatus5XX).filter_by(**filters)
        return res.all()


class TestMySql(MyTest):

    def test_add_requests_amount(self):
        self.builder.add_requests_amount()
        count = self.get_from_requests_amount()
        assert len(count) == 1

    def test_add_requests_amount_by_types(self):
        self.builder.add_requests_amount_by_types()
        types_amount = len(self.builder.analyzer.methods.get_request_types())
        count = self.get_from_requests_amount_by_type()
        assert len(count) == types_amount

    @pytest.mark.parametrize("top", [10])
    def test_add_most_frequent_requests(self, top):
        self.builder.add_most_frequent_requests(top)
        count = self.get_from_most_frequent_requests()
        assert len(count) == top

    @pytest.mark.parametrize("top", [10])
    def test_add_biggest_requests_with_request_status_4XX(self, top):
        self.builder.add_biggest_requests_with_request_status_4XX(top)
        count = self.get_from_biggest_requests_with_request_status_4XX()
        assert len(count) == top

    @pytest.mark.parametrize("top", [5])
    def test_add_top_users_by_amount_of_requests_with_status_5XX(self, top):
        self.builder.add_top_users_by_amount_of_requests_with_status_5XX(top)
        count = self.get_from_top_users_by_amount_of_requests_with_status_5XX()
        assert len(count) == top
