from marshmallow import EXCLUDE, fields, Schema

from apis.schemas import validate_one_word


fields.Field.default_error_messages['required'] = 'is a required field'


class UserCreatePayloadSchema(Schema):
    """
    Schema on which user create payload will be validated
    """

    class Meta:
        unknown = EXCLUDE  # to ignore unknown fields

    first_name = fields.Str(required=True, validate=validate_one_word)
    last_name = fields.Str(required=True, validate=validate_one_word)
    username = fields.Str(required=True, validate=validate_one_word)
    password = fields.Str(required=True, validate=validate_one_word)
    email = fields.Email()
