import pytest

from mysql.client import MysqlClient
from parsers.log_analyzer import LogAnalyzer


def pytest_configure(config):
    mysql_client = MysqlClient(db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()

    mysql_client.connect(db_created=True)
    mysql_client.create_table("requests_amount")
    mysql_client.create_table("requests_amount_by_type")
    mysql_client.create_table("most_frequent_requests")
    mysql_client.create_table("biggest_requests_with_request_status_4XX")
    mysql_client.create_table("top_users_by_amount_of_requests_with_status_5XX")
    mysql_client.connection.close()


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = MysqlClient(db_name='TEST_SQL')
    client.connect()
    yield client
    client.connection.close()


@pytest.fixture(scope='session')
def log_analyzer() -> LogAnalyzer:
    analyzer = LogAnalyzer()
    return analyzer

