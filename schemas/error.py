from flask_openapi3 import Schema


class ErrorSchema(Schema):
    """
    Defines how an error message will be represented.
    \f
    :param message: The error message.
    """
    message: str
