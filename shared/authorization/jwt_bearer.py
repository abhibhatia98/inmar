from typing import Dict, List

import jwt
from pydantic import BaseModel


class JWTBearer:
    def __init__(self):
        # store it in a safe place like key vault
        self.jwt_signing_key = '{"d": "SppZFqqwRC6B_R91EVL4D-g4sHjzcafet-9mFN5qFz9EVWdNK8ys6xzePr1XOsyMT4dpb6EILR4nGr7a3o53yj61kc7RKJA4C7OOvBjTwcIeJ9SvLt-t2M-2PXdllykrhLhLwEE0i8VwUf-FCzIf3ZV_KRWSvJXNuE7Gmb7iYeLIUE2ylf6TWtQC6MVHIwUv4kaJ9N2mj4jYbtI1WsECvlbdBK6rp8p6sXWab73tD0WkJEqGwsRRwjOa8KTl-zDg-OKP7eni3yzN8bKrYgJvJ3CDgiqvAoww64TT5vTsmUMCMwZl4eHGFYSeOHwD0fYjUkuYt-sHyhfL_wilZHJJgQ", "dp": "WJzEwumhYV-eIsUTEt7Tmlgv9LlIwp4U1sI71U12j9KmI1WWobXDgxKJcfDfztQqply2yvfCGwVcXOV1CCoG8SQRlUJ6YPD6pmL6bvSCZri-QR9bCAeXah0SR7nwrON6tIsedk1EiECC2U38QH3UV2oI5_LhdOEKCoIxvhHIWME", "dq": "C1gHSOTO1HlOQ4_cdQI55AF7na52Q6tw2Vls8Me65AR7inAECfGp2W8jDS6L8OZQRxraInaQ3JsBSkuz__ZOb3iYjJfC5DCkPjdyxrWG1oEwMBVA5tHqXfeOr61yS7HqB74EAZCVrTSXrg-_6isN1PbP5g2RWpGdrETBBXqAh8E", "e": "AQAB", "kty": "RSA", "n": "w5ny-6e_QuLFqOt_iXFzWa2-ydFrkFvuysPhunweNZkg8ahwm5whgitGS2pJk84X91psTkV6Ly0lvUkZ0slf6PYgCohI_v1s42a6ZO_mDb408uD6bIy6PS3U9Mq725vnueeBvyjkj_oPj8AAHBgznWhO-A9cUdtRTJzPDODy2477hPKETpUYrNn4atdMsPbs59kasZvdMeUHWhGIL7Mdkz_nZT9qmVD5ZZmhvZGt0zpVNYlh9L59LellcDWB7k10Mwp2opXwpK-UlcsvT8NRgOlyold73KHREI4HaLohLSgiZt9XJd_r3sn3v4qlmI4R6gReNy1erpXDHJZGN8-bxQ", "p": "4Tt3YPeLMIqE_O8jvhe78N3eSpijQ_rU6wWBn6pVmP4Szf8lUyBhJmyf2xanl6tsNSG6p71oy2midHYNALSc52gomflTCZCYvGHdY1r1tM_WACKXyGz4oUkeT2Q-Vxh1yyh1kbXDDaHoRMs8HNp6X3UpPk9dFql9sStAa2xTWKk", "q": "3lJEqfWRPxd7eR6fm3WBFusl6EYeyQLLsmTr9VVpA6Bs7oLyEFwoC7Y89lLD8D_Irsj5q4lw7okGh7tGthJAItW-QPFDDvgSSSm40N2D-7cE_zESEpbATBcEOn-J4uzXF-OAlI_diL90kRrK3VF0XXJJQLmGIoYklZ8G6GJzT70", "qi": "ol8m-s-uckQ1T19TgFqAjtZPfsNozyo1BgHCoA0hU9PM17vd_jpm-VVn5l3VebFgkY2_kDJSdj5Q6swBCi24sUehquq7COSZx5WH_fY6F6mYqUmtAZ5AdawtKCjyVTyv0NYtLDuG1FB0N2svYRo_jq-NRbRVhPtCRRw47OOQDo4", "kid": "3CFE46595E32D191A65B519BEE892B6CDD6D8D87FF933FD2E56D8BBA07F6E2CA"}'

    def generate_token(self, payload: dict, algorithm):
        return jwt.encode(payload, self.jwt_signing_key, algorithm=algorithm)

    def verify_token(self, token, algorithem):
        return jwt.decode(token, key=self.jwt_signing_key, algorithms=algorithem)



