import boto3
import json
import os


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['tableName'])

    data = json.loads(event['body'])

    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Credentials": True
    }

    response = table.update_item(
        Key = {
            'user_id': event['requestContext']['identity']['cognitoIdentityId'],
            'note_id': event['pathParameters']['id']
        },
        UpdateExpression="set content = :content",
        ExpressionAttributeValues={
            ':content': data['content']
        },
        ReturnValues = "UPDATED_NEW"
    )

    return {
        "statusCode": 200,
        "headers": headers,
        "body" : json.dumps(response)
    }

