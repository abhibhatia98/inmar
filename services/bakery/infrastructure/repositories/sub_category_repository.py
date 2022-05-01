from injector import singleton
from bakery.infrastructure.repository import Repository


@singleton
class SubCategoryRepository(Repository):

    pass