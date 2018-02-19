"""
This is the entry point to server
Author: https://github.com/velutha
"""
import os
from flask import request, jsonify
from src import app
from src.validator import Validator
from src.controllers.user_controller import UserController
from src.logger import logger


@app.route("/bot/health")
def hello_world():
    status_message = {"status": "UP"}
    return jsonify(status_message)


@app.route("/user", endpoint="get_session")
@Validator.validate_user
def get_session():

    logger.info("Session route hit")
    user_id = request.args.get("user_id")
    response = UserController.get(user_id)

    return response


if __name__ == "__main__":
    HOST = os.environ.get("HOST") or "0.0.0.0"
    PORT = os.environ.get("PORT") or 9500
    PORT = int(PORT)
    app.run(host=HOST, port=PORT)
