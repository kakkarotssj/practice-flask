import json

from flask import request
from flask_restplus import Resource

from .schemas import UserCreatePayloadSchema
from apis.validate_request import ValidateRequest
from commons.response import Response


class User(Resource):
    """
    This resource will handle all operations on User
    """

    def post(self):
        """
        Handles user creation
        :return: return serialized response
        """

        response = Response()

        request_validators = [
            {'payload': {'data': json.loads(request.data), 'schema': UserCreatePayloadSchema}},
        ]
        ValidateRequest.validate(response, request_validators)
        if response.errors:
            response.message = "Invalid Request"
        else:
            #  call some activity from here
            pass

        if not response.errors:
            response.status_code = 200

        return response.to_dict()
