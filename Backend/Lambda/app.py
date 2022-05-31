'''
Purpose: 

This helper increments and retrieves the value of a simple atomic counter stored in a DynamoDB table. 

Table has a very simple schema:

TableName: resSiteCounter
PrimaryKey: pk (S)
Attribute: visitors (N)
'''
import json
import boto3
import os


# initialize and set resources
dynamodb = boto3.resource('dynamodb')
dbtable = os.environ['table'] 
table = dynamodb.Table(dbtable)

def lambda_handler(event, context):
    # increment the count or add if not present
    ddbResponse = table.update_item(
        Key = {
            'id': 'visitors',
        },  
        ExpressionAttributeValues = {
            ':INCR': 1,
            ':start': 0,
        },
        ExpressionAttributeNames = {
            '#V': 'count',
        },
        UpdateExpression = 'SET #V = if_not_exists(#V, :start) + :INCR',
        ReturnValues = 'UPDATED_NEW'
    )

    # variableize it up to the max!
    responseBody = int(ddbResponse["Attributes"]["count"])

    # build response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS" 
        },
    }

    # return response object
    return apiResponse