import json
from functools import wraps
from starlette.requests import Request
from shared.authorization.context import Context
from fastapi import HTTPException
from shared.authorization import injector
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from typing import List
from shared.reader.config_reader import ConfigReader
from bson import ObjectId
from shared.authorization.jwt_bearer import JWTBearer
bearer = injector.get(JWTBearer)


def auth_required():

    def decorator(func):
        @wraps(func)
        def wrapper(request: Request, *args, **kwargs):
            """
            Method has access to request object to get organization id and match it with id from token
            :param request: request object used in fast API
            :param args:
            :param kwargs:
            :return:
            """
            credentials = request.headers.get("x-authorization", None)
            if credentials:
                try:
                    auth_type, token = credentials.split(" ")
                    if auth_type != "Bearer":

                        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
                    # verify token
                    claims = bearer.verify_token(token,"HS256")
                except Exception as ex:
                    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
                data = {"user": claims["user_id"],
                        "user_email": claims["user_email"],
                        "token": credentials,
                        "trace_id": request.headers.get('trace_id', str(ObjectId())),
                        }
                user_context = Context(**data)
                kwargs["context"] = user_context
            else:
                raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="NOT AUTHORIZED")
            return func(request, *args, **kwargs)
        return wrapper
    return decorator
