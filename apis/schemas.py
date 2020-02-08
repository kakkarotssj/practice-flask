from marshmallow import ValidationError


def validate_one_word(string):
    if len(string.split(' ')) > 1:
        raise ValidationError('Only word allowed in this field')
