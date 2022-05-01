from injector import singleton

from bakery.domain.model.location import MediaTask
from bakery.infrastructure.repository import Repository


@singleton
class DepartmentRepository(Repository):

    def add(self, media_task: MediaTask):
        media_task.save()
