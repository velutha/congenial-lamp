import os

application_config = {
    "QUEUE_URL" : os.environ.get("QUEUE_URL"),
    "AWS_ACCESS_KEY_ID" : os.environ.get("AWS_ACCESS_KEY_ID"),
    "AWS_ACCESS_SECRET_KEY" : os.environ.get("AWS_ACCESS_SECRET_KEY"),
    "AWS_REGION" : os.environ.get("AWS_REGION"),
    "KINESIS_STREAM_NAME": os.environ.get("KINESIS_STREAM_NAME"),
    "ENVIRONMENT": os.environ.get("ENVIRONMENT"),
    "IS_AWS_ENABLED": os.environ.get("IS_AWS_ENABLED") == "TRUE" or False,
    }
