import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table(os.environ['tableName'])

def lambda_handler(event, context):
    
    data = json.loads(event['body'])

    item = {
        'user_id': event['requestContext']['identity']['cognitoIdentityId'],
        'note_id': str(uuid.uuid1()),
        'content': data['content']
    }

    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Credentials": True
    }

    try:     
        table.put_item( Item = item)
    except Exception:
        response = {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps(item)
            }
        return response

    response = {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(item)
    }

    return response





# Changes made
# Import os, use os for table name
# remove hardcoded user id and note id values
# modified userId and noteId to user_id and note_id
# changed note_text: data to content: data['content]
# changed headers
# changed json.dumps to item instead of data


    