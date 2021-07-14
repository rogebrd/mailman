import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    params = event['queryStringParameters']
    email = params['email']
    dropbox_oauth_token = params['dropbox_oauth_token']

    dynamodb.put_item(
        TableName='Registrations',
        Item={
            'email': {'S': email},
            'dropbox_oauth_token': {'S': dropbox_oauth_token},
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
