'''
Test for app.py visitor counter function.
'''
 
import boto3
import os
import unittest
from moto import mock_dynamodb
import app

def mock_resources():
    # fake AWS creds for moto testing
    os.environ['AWS_ACCESS_KEY_ID'] = 'fakerson'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'fakerson'
    os.environ['AWS_SECURITY_TOKEN'] = 'fakerson'
    os.environ['AWS_SESSION_TOKEN'] = 'fakerson'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

    # db table env var
    os.environ['table'] = 'testdb'

class test_lambda(unittest.TestCase):
    @mock_dynamodb
    def test_lambda_handler(self):
        # set up boto3 ddb
        dynamodb = boto3.client('dynamodb')
        # pull table name
        table = os.environ['table']
        # set up mock table
        dynamodb.create_table(
            TableName = table,
            BillingMode = 'PAY_PER_REQUEST',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ]
        )

        response = app.lambda_handler(0, 0)
        print("Lambda function response: ", response)

        # check response against expected 200 ok
        self.assertEqual(200, response['statusCode'])

if __name__ == '__main__':
    mock_resources()
    unittest.main()