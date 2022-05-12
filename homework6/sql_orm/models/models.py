from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class RequestsAmountModel(Base):
    __tablename__ = 'requests_amount'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Requests Amount: {self.amount}>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer)


class RequestsAmountByTypeModel(Base):
    __tablename__ = 'requests_amount_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    requests_type = Column(String(500))
    requests_amount = Column(Integer)


class MostFrequentRequests(Base):
    __tablename__ = 'most_frequent_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    request_url = Column(String(50))
    request_amount = Column(Integer)


class BiggestRequestsWithRequestStatus4XX(Base):
    __tablename__ = 'biggest_requests_with_request_status_4XX'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    request_url = Column(String(300))
    status_code = Column(Integer)
    request_size = Column(Integer)
    user_ip = Column(String(20))


class TopUsersByAmountOfRequestsWithStatus5XX(Base):
    __tablename__ = 'top_users_by_amount_of_requests_with_status_5XX'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_ip = Column(String(20))
    requests_amount = Column(Integer)