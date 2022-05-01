from shared.authorization.jwt_bearer import JWTBearer

temp = JWTBearer()
token = temp.generate_token(payload={"user_id": "626d38970b9eabe51bb35a65", "user_email": "test@gmail.com"},
                            algorithm="HS256")
print(token)
