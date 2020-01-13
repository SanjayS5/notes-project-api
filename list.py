import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(os.environ['tableName'])

    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Credentials": True
    }

    result = table.scan()
    
    response = {
       "statusCode": 200,
       "headers": headers,
       "body": json.dumps(result["Items"])
    }

    return response