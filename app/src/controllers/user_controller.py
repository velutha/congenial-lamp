"""
User controller
Author: https:github.com/velutha
"""
from flask import jsonify
from src.models.user import User

class UserController():

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get(user_id):
        user_data = User(user_id).find()
        return jsonify(user_data)
