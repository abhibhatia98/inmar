from fastapi import status, Depends, Query
from starlette.requests import Request

from bakery.application.commands.location.add_location_command import AddLocationsCommand
from bakery.application.commands.location.delete_location_command import DeleteLocationCommand
from bakery.application.commands.location.update_location_command import UpdateLocationCommand
from bakery.application.queries.location_queries import LocationQueries
from bakery_api import router, injector
from shared.application.custom_types.oid import OID

# from shared.authorization.auth import auth_required
#
from shared.integration.mediator import Mediator

location_queries = injector.get(LocationQueries)
mediator = injector.get(Mediator)

@router.get("/", status_code=status.HTTP_200_OK)
def get_version(request: Request, context=None):
    return {'version': "v1.0.0"}


@router.get("/location", status_code=status.HTTP_200_OK)
def get_location(request: Request, context=None, page_size=10, skip=0):
    return location_queries.get_locations(page_size=page_size, skip=skip)


@router.post("/location", status_code=status.HTTP_200_OK)
def add_location(request: Request, command: AddLocationsCommand, context=None):
    return mediator.send(command)


@router.put("/location", status_code=status.HTTP_200_OK)
def update_location(request: Request, command: UpdateLocationCommand, context=None):
    return mediator.send(command)


@router.delete("/location", status_code=status.HTTP_200_OK)
def delete_location(request: Request, command: DeleteLocationCommand, context=None):
    return mediator.send(command)
