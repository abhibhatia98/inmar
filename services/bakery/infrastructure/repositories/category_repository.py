from mongoengine import EmbeddedDocument, Document

from services.bakery.infrastructure.repository import Repository


class CategoryRepository(Repository):

    def add(self, organization_category: OrganizationCategory):
        organization_category.save()
        organization_category.category_created()
        self.dispatch(organization_category)