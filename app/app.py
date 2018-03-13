"""
This is the entry point to server
Author: https://github.com/velutha
"""
import os
import traceback
from flask import request, jsonify
from werkzeug.exceptions import HTTPException
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


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    logger.error(traceback.format_exc())
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

if __name__ == "__main__":
    HOST = os.environ.get("HOST") or "0.0.0.0"
    PORT = os.environ.get("PORT") or 9500
    PORT = int(PORT)
    app.run(host=HOST, port=PORT)
