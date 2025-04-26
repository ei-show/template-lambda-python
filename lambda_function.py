import base64
import gzip
import json
import os
import boto3
import urllib.request
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv(override=False)

# Set up logging
import setup_log # setup_log.py
logger = setup_log.logger
# Set the log level from environment variable or default to INFO
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logger.setLevel(log_level)
logger.debug("Starting Lambda execution")

def lambda_handler(event, context):
    """Lambda function entry point
    Args:
        event: event
        context: context
    Returns:
        dict: response
    """
    logger.debug("Received event: %s", json.dumps(event))
    logger.info("Processing event")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
