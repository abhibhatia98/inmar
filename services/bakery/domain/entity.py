from enum import Enum

from bakery import Base
from sqlalchemy import orm


class EntityOperationStatus(Enum):
    """
    defines different operation status
    """

    NONE = 0
    ADDED = 1
    UPDATED = 2
    DELETED = 3


class Entity(Base):
    """
    define an base class for all the entities in service
    """

    __abstract__ = True
    operation_status = EntityOperationStatus.NONE.value

    # domain_events = []

    def __init__(self, **data):
        super().__init__(**data)
        self.domain_events = []
        self.trace_id = None

    @orm.reconstructor
    def init_on_load(self):
        """
        This has been added as sqlalchemy does not call init on
        initializing docs when querying from db
        :return:
        """
        self.domain_events = []
        self.trace_id = None

    def add_domain_event(self, event):
        """
        used to add domain events
        :param event:
        :return:
        """
        self.domain_events.append(event)

    def clear_events(self):
        """

        :return:
        """
        self.domain_events = []

    def get_events(self):
        """

        :return:
        """
        return self.domain_events
