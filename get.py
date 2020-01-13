import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import os

def lambda_handler(event, context):
    
    dynamodb = boto3.resource("dynamodb")
    
    table = dynamodb.Table(os.environ['tableName'])
    
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Credentials": True
    }

    try:
        response = table.get_item(
            Key={
                'user_id': event['requestContext']['identity']['cognitoIdentityId'],
                'note_id': event['pathParameters']['id']
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else: 
        item = response['Item']
        # print("GetItem succeeded:")
        # print(json.dumps(item))
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(item)
        }
        
