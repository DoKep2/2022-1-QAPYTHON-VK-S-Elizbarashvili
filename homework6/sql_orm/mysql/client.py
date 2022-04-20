import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from models.models import Base


class MysqlClient:

    def __init__(self, db_name):
        self.user = 'root'
        self.port = 3306
        self.password = '0000'
        self.host = '127.0.0.1'
        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):

        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database IF EXISTS {self.db_name}')
        self.execute_query(f'CREATE database {self.db_name}')

    def create_table(self, table_name):
        if not inspect(self.engine).has_table(table_name):
            Base.metadata.tables[table_name].create(self.engine)

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

