from marshmallow import ValidationError


class ValidateRequest:
    """
    Validator class that provides common and basic requests validation
    """

    @classmethod
    def validate(cls, response, request_validators=None):
        """
        :param response: response object, will include errors(if any) in request
        :param request_validators: list of validators
            each index of list will be a dict where key defines request part and value will again be a dict of two
            keys where data and schema are defined
        :return valid deserialized request
        """
        valid_request = {}

        for request_validator in request_validators:
            for request_part, validator in request_validator.items():
                data = validator['data']
                schema = validator['schema']
                try:
                    result = schema().load(data)
                    valid_request[request_part] = result
                except ValidationError as error:
                    response.errors = error.messages

        return valid_request
