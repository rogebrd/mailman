import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    params = event['queryStringParameters']
    email = params['email']
    password = params['password']

    dynamodb.put_item(
        TableName='Emails',
        Item={
            'email': {'S': email},
            'password': {'S': password},
        }
    )

    response = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': 'Email {} registered!'.format(email)
        }

    print('Response: %s' % (response))
    return response
