from fastapi import status
from starlette.requests import Request

from bakery.application.commands.category.add_category_command import AddCategoryCommand
from bakery.application.commands.category.delete_category_command import DeleteCategoryCommand
from bakery.application.commands.category.update_category_command import UpdateCategoryCommand
from bakery.application.commands.department.add_department_command import AddDepartmentsCommand
from bakery.application.commands.department.delete_department_command import DeleteDepartmentCommand
from bakery.application.commands.department.update_department_command import UpdateDepartmentCommand
from bakery.application.commands.location.add_location_command import AddLocationsCommand
from bakery.application.commands.location.delete_location_command import DeleteLocationCommand
from bakery.application.commands.location.update_location_command import UpdateLocationCommand
from bakery.application.queries.category_queries import CategoriesQueries
from bakery.application.queries.department_queries import DepartmentQueries
from bakery.application.queries.location_queries import LocationQueries
from bakery_api import router, injector
# from shared.authorization.auth import auth_required
#
from shared.integration.mediator import Mediator

location_queries = injector.get(LocationQueries)
department_queries = injector.get(DepartmentQueries)
categories_queries = injector.get(CategoriesQueries)

mediator = injector.get(Mediator)


@router.get("/location", status_code=status.HTTP_200_OK)
def get_location(request: Request, context=None, page_size=10, skip=0):
    return location_queries.get_locations(page_size=page_size, skip=skip)


@router.post("/location", status_code=status.HTTP_200_OK)
def add_location(request: Request, command: AddLocationsCommand, context=None):
    return mediator.send(command)


@router.put("/location/{location_id}", status_code=status.HTTP_200_OK)
def update_location(request: Request,location_id:str,command: UpdateLocationCommand, context=None):
    command.set_location_id(location_id)
    return mediator.send(command)


@router.delete("/location/{location_id}", status_code=status.HTTP_200_OK)
def delete_location(request: Request, location_id: str, context=None):
    command = DeleteLocationCommand()
    command.set_location_id(location_id)
    return mediator.send(command)


@router.get("/location/{location_id}/department", status_code=status.HTTP_200_OK)
def get_location_departments(request: Request, location_id: str, context=None, page_size=10, skip=0):
    return department_queries.get_departments(location_id=location_id, page_size=page_size, skip=skip)


@router.post("/location/{location_id}/department", status_code=status.HTTP_200_OK)
def add_location_departments(request: Request, location_id: str, command: AddDepartmentsCommand, context=None):
    command.set_location_id(location_id)
    return mediator.send(command)


@router.put("/location/{location_id}/department/{department_id}", status_code=status.HTTP_200_OK)
def update_location_departments(request: Request, location_id: str, department_id: str,
                                command: UpdateDepartmentCommand, context=None):
    command.set_location_id(location_id)
    command.set_department_id(department_id)
    return mediator.send(command)


@router.delete("/location/{location_id}/department/{department_id}", status_code=status.HTTP_200_OK)
def delete_location_departments(request: Request, location_id: str, department_id: str, context=None):
    command = DeleteDepartmentCommand()
    command.set_location_id(location_id)
    command.set_department_id(department_id)
    return mediator.send(command)


# point c

@router.get("/location/{location_id}/department/{department_id}/category", status_code=status.HTTP_200_OK)
def get_department_categories(request: Request, location_id: str, department_id: str, context=None, page_size=10,
                              skip=0):
    return categories_queries.get_department_categories(location_id=location_id, department_id=department_id,
                                                        page_size=page_size, skip=skip)


@router.post("/location/{location_id}/department/{department_id}/category", status_code=status.HTTP_200_OK)
def add_departments_categories(request: Request, location_id: str, department_id: str, command: AddCategoryCommand,
                               context=None):
    command.set_location_id(location_id)
    command.set_department_id(department_id)
    return mediator.send(command)


@router.put("/location/{location_id}/department/{department_id}/category/{category_id}", status_code=status.HTTP_200_OK)
def update_departments_categories(request: Request, location_id: str, department_id: str, category_id: str,
                                  command: UpdateCategoryCommand, context=None):
    command.set_location_id(location_id)
    command.set_category_id(category_id)
    command.set_department_id(department_id)
    return mediator.send(command)


@router.delete("/location/{location_id}/department/{department_id}/category/{category_id}",
               status_code=status.HTTP_200_OK)
def delete_location_departments(request: Request, location_id: str, department_id: str, category_id: str, context=None):
    command = DeleteCategoryCommand()
    command.set_location_id(location_id)
    command.set_department_id(department_id)
    command.set_category_id(category_id)
    return mediator.send(command)
