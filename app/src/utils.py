# from functools import reduce
import json
import uuid
import time
import requests
from jsonpath import jsonpath
from src.logger import logger

class Util(object):

    @staticmethod
    def merge_dicts(*args):
        result = {}
        for dictionary in args:
            logger.debug("Merging dictionaries")
            logger.debug(f"{dictionary} {dictionary.__class__}")
            result.update(dictionary)
        return result

    @staticmethod
    def deep_find(obj, path):
        try:
            val = jsonpath(obj, path)
            if bool(val) and isinstance(val, list) and len(val) == 1:
                val = val[0]
            return val
        except Exception as err:
            logger.error(err)
            return None
