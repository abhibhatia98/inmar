import json
from functools import wraps
from starlette.requests import Request
from shared.authorization.jwt_bearer import JWTBearer
from shared.constant.jwt_constants import JWTConstants
from shared.authorization.context import Context
from fastapi import HTTPException
from shared.authorization import injector
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from typing import List
from shared.reader.config_reader import ConfigReader
from bson import ObjectId
bearer = injector.get(JWTBearer)


def auth_required(permission, mandatory_permissions: List = None):
    """
    Decorator for role based route protection
    The route using this decorator need to pass request: Request in the handler function too
    :param mandatory_permissions: List of permissions in which user shall have all
    :param permission: Class with two attributes
                       Service - defining service for which permissions are
                       Permissions - List of permission for the service which are needed
    :return: Wrapper for route and passes a kwarg context with user data else blocks the request with
             a 401
    """
    # because of https://docs.python-guide.org/writing/gotchas/
    # mutable default arguments (We are not doing any mutation so not necessarily needed)
    # but can cause problem if not aware
    if mandatory_permissions is None:
        mandatory_permissions = []

    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            """
            Method has access to request object to get organization id and match it with id from token
            :param request: request object used in fast API
            :param args:
            :param kwargs:
            :return:
            """
            # print(permission, "tied")
            # for header in request.headers:
            #     print(header, request.headers.get(header, None))
            credentials = request.headers.get("x-authorization", None)
            if credentials:
                try:
                    auth_type, token = credentials.split(" ")
                    # First the credentials are verified
                    # using claims from the token claims
                    # by checking organization and checking if any permission required for accessing the route
                    # is there in the token permissions is yes context is set and execution continues
                    if auth_type != "Bearer":
                        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
                    key = json.loads(ConfigReader.read_config_parameter("jwt_verification_key"))
                    claims = bearer.verify_custom_token(jwt_token=token, audience=JWTConstants.AUDIENCE,
                                                        issuer=JWTConstants.ISSUER,
                                                        key=key)
                except Exception as ex:
                    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
                permissions_from_token = set(claims["permissions"])
                organization_id_from_token = claims["organization_id"]
                organization_id_from_url = request.path_params["organization_id"]
                if organization_id_from_url != organization_id_from_token:
                    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="FORBIDDEN")
                services_with_permissions_allowed = set(permission.service + "." + service_permission
                                                        for service_permission in permission.permissions)

                permission_intersection = permissions_from_token.intersection(services_with_permissions_allowed)
                if services_with_permissions_allowed:
                    if permission_intersection == set():
                        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="FORBIDDEN")

                # check for man. permission
                mandatory_permissions_required = set(permission.service + "." + mandatory_permission
                                            for mandatory_permission in mandatory_permissions)
                for mandatory_permission in mandatory_permissions_required:
                    if mandatory_permission not in permissions_from_token:
                        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="FORBIDDEN")

                filtered_permissions = list(".".join(filtered_permission.split(".")[1:]) for
                                            filtered_permission in permissions_from_token
                                            if filtered_permission.split(".")[0] == permission.service)

                data = {"user": claims["user_id"],
                        "permissions": filtered_permissions,
                        "user_sub": claims["user_sub"],
                        "user_email": claims["user_email"],
                        "user_role": claims["user_role"],
                        "token": credentials,
                        "organization_id": organization_id_from_url,
                        "trace_id": request.headers.get('trace_id', str(ObjectId())),
                        'exat': claims['exat']
                        }
                user_context = Context(**data)

                # user_context given as a kwarg so every route using this needs to
                # specify a keyword argument in the function handling the route USE context=None instead
                # of context: Context as doing this will expose the context with all the data in docs and openapi
                kwargs["context"] = user_context
            else:
                raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="NOT AUTHORIZED")
            return await func(request, *args, **kwargs)

        return wrapper

    return decorator
