import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table(os.environ['tableName'])
    
    table.delete_item(
        Key={
            'user_id': event['requestContext']['identity']['cognitoIdentityId'],
            'note_id': event['pathParameters']['id'],
        }
    )

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True
        }
    }

    return response