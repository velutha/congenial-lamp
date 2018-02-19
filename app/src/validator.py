"""
All validators for apis go here
Author: https://github.com/velutha
"""
from functools import wraps
from flask import request, jsonify

class Validator():
    """
    Main validator class. This class can accept for every
    param validation and can be distributed here
    """

    def __init__(self):
        pass


    @staticmethod
    def validate_user(func):
        @wraps(func)
        def validate_session(*args, **kwargs):
            user_id = request.args.get("user_id")
            if user_id is None:
                response = jsonify(message="Required param missing"), 400
                return response
            return func(*args, **kwargs)
        return validate_session
