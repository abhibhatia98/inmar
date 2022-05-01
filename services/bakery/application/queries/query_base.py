from injector import inject
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.util.compat import contextmanager

from shared.reader.config_reader import ConfigReader


class QueryBase:
    """
    base class for query
    """

    @inject
    def __init__(self):
        # self.user_name = ConfigReader.read_config_parameter("db_postgres_user_name")
        # self.password = ConfigReader.read_config_parameter("db_postgres_password")
        # self.database = ConfigReader.read_config_parameter("db_postgres_name")
        # self.url = ConfigReader.read_config_parameter("db_postgres_url")
        # self.engine = create_engine(
        #     self.url.format(self.user_name, self.password, self.database)
        # )
        self.engine = create_engine("postgresql://postgres:123456789@localhost:5432/bakery")

    @contextmanager
    def session_scope(self):
        """
        creates an session object
        :return:
        """
        session = Session(self.engine)
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
