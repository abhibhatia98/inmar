from injector import inject
from bakery import Base
from bakery.domain.entity import Entity
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.util.compat import contextmanager

from shared.integration.mediator import Mediator
from shared.reader.config_reader import ConfigReader


class BaseRepository:
    """
    This class defines soe common methods that are useful for all the
    other repository file in service
    """

    @inject
    def __init__(self, mediator: Mediator):
        """
        responsible for creating database connection
        :param mediator:
        """
        self.mediator = mediator
        # self.user_name = ConfigReader.read_config_parameter("db_postgres_user_name")
        # self.password = ConfigReader.read_config_parameter("db_postgres_password")
        # self.database = ConfigReader.read_config_parameter("db_postgres_name")
        # self.url = ConfigReader.read_config_parameter("db_postgres_url")
        # self.engine = create_engine(
        #     self.url.format(self.user_name, self.password, self.database)
        # )
        self.engine = create_engine("postgresql://postgres:123456789@localhost:5432/bakery")

        Base.metadata.create_all(self.engine)

    @contextmanager
    def session_scope(self, isolation_level: str = None):
        """
        this method return an db session
        :param isolation_level:
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

