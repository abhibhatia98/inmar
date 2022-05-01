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

    def dispatch(self, entity: Entity):
        """
        this method call handlers for all the registered events
        :param entity:
        :return:
        """
        events = entity.get_events()
        for event in events:
            self.mediator.send(event)
        entity.clear_events()

    def save(self, session):
        """
        it commit the changes in db and close the session
        :return:
        """
        session.commit()
        session.close()

    def add(self, entity, session: Session = None) -> None:
        """
        it adds the specified entity to db in pending state
        This is required as organization id foreign key that has to be in db for adding other
        its dependent entity like department and other
        :param entity: value which needs to be added to db
        :return:
        """
        session.add(entity)
        session.flush()
        self.dispatch(entity)

    def commit_entity(self, entity, session: Session) -> None:
        """
        This method commit the changes to db for the entity tha has session attached
        :param entity:
        :param session:
        :return:
        """
        session.add(entity)
        session.commit()

    def bulk_add(self, entities):
        """
        it adds the specified entity value to db
        :param entities: value which needs to be added to db
        :return:
        """
        # with self._make_session() as session:
        with self.session_scope() as session:
            session.bulk_save_objects(entities)

    def bulk_add_in_transaction(self, entities, transaction_session):
        """
        :param entities:
        :param transaction_session:
        :return:
        """
        transaction_session.bulk_save_objects(entities)

    def add_in_transaction(self, entity, transaction_session):
        """
        This method add an entity to db with transaction session
        :param entity:
        :param transaction_session:
        :return:
        """
        transaction_session.add(entity)
