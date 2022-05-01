from typing import Dict, List

from jose import jwt, jwk
from jose.utils import base64url_decode

from pydantic import BaseModel

from starlette.requests import Request

from shared.constant.jwt_constants import JWTConstants


JWK = Dict[str, str]


class JsonWebKeys:
    keys: List[JWK]


class JWTAuthorizationCredentials(BaseModel):
    jwt_token: str
    header: Dict[str, str]
    signature: str
    message: str


class JWTBearer:
    def __init__(self):
        pass

    def verify_b2c_token(self, request: Request, audience: str, issuer: str, json_web_keys_list: List):
        """
        Method for verifying the token received from b2c
        :param request: request object from azure functions
        :param audience: Audience for which token was issued
        :param issuer: Issuing authority
        :param json_web_keys_list: List of json web keys
        :return: Decoded claims from token if every thing is correct
        """
        try:
            credentials = request.headers.get("Authorization")
            bearer, jwt_token = credentials.split(" ")
            if bearer != "Bearer":
                raise ValueError("Invalid authorization method")
            header = jwt.get_unverified_headers(jwt_token)
            if header['alg'] != JWTConstants.ALGORITHMS_RS256:
                return ValueError("Invalid algorithm")
            kid_to_jwk = {json_web_key["kid"]: json_web_key for json_web_key in json_web_keys_list}
            public_key = kid_to_jwk[header["kid"]]
        except Exception as ex:
            #TODO: revisit
            raise ex
        return self.__verify_jwt_token(jwt_token=jwt_token,
                                       audience=audience,
                                       issuer=issuer, public_key=public_key)

    def verify_custom_token(self, jwt_token: str, audience: str, issuer: str, key: dict):
        """
        Method to verify custom token
        :param jwt_token: token
        :param audience: audience
        :param issuer: issuer
        :param key: public verification key
        :return:
        """
        try:
            return self.__verify_jwt_token(jwt_token=jwt_token,
                                           audience=audience,
                                           issuer=issuer, public_key=key)
        except Exception as ex:
            raise ex

    @staticmethod
    def __verify_jwt_token(jwt_token: str, audience: str,
                           issuer: str, public_key: dict):
        """
        Method to verify jwt token and return decoded claims
        :param jwt_token: token
        :param audience: audience
        :param issuer: issuer
        :param public_key: key to be used for verification
        :return:
        """
        try:
            # can be user for signature verification for step by step claims handling
            # currently decode throws exception for each claim not being met
            header = jwt.get_unverified_headers(jwt_token)
            public_jwk_key = jwk.construct(public_key, algorithm=header["alg"])
            message, signature = jwt_token.rsplit(".", 1)
            decoded_signature = base64url_decode(signature.encode())
            verified = public_jwk_key.verify(message.encode(), decoded_signature)
            decoded = jwt.decode(
                jwt_token,
                key=public_key,
                algorithms=header["alg"],
                audience=audience,
                issuer=issuer
            )
        except Exception as ex:
            raise ex
        return decoded

    @staticmethod
    def create_token(payload: dict, key: str, algorithm=JWTConstants.ALGORITHMS_RS256):
        """
        Method to create a jwt_token
        :param algorithm: by default set to RS256
        :param payload: dict object containing the data to be encoded in token
        :param key: Private Signing KEY
        :return: JWT token
        """
        return jwt.encode(claims=payload, key=key, algorithm=algorithm)
