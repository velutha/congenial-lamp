"""
Application init file
"""
import os
import redis
import pymongo
from pymongo import MongoClient
from flask import Flask
from src.logger import logger
from src.connectors.redis_helper import RedisHelper
from src.thread_pool import ThreadPoolExecutorStackTraced

app = Flask(__name__)

# CACHE = RedisHelper().create_client()

DB_CONNECTION = os.environ.get("DB_CONNECTION") or "mongodb://localhost:27017/my_db"

MONGO_CLIENT = MongoClient(DB_CONNECTION)

ThreadPool = ThreadPoolExecutorStackTraced(max_workers=20)

try:
    MONGO_CLIENT.server_info()
    # insert db name here
    DB = MONGO_CLIENT["DB_NAME"]
    logger.info("Connected to DB")

except pymongo.errors.ServerSelectionTimeoutError as err:
    logger.error("Error connecting to mongodb\n" + str(err))
    raise

except:
    logger.critical("Server could not start.\n Unexpected error occured")
    raise
