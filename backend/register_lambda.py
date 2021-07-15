import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    params = event['queryStringParameters']
    if 'email' not in params or 'dropbox_oauth_token' not in params:
        response = create_response(400, 'Missing info for registration.')
        return response
    email = params['email']
    dropbox_oauth_token = params['dropbox_oauth_token']

    try:
        dynamodb.put_item(
            TableName='Registrations',
            Item={
                'email': {'S': email},
                'dropbox_oauth_token': {'S': dropbox_oauth_token},
            }
        )
    except:
        response = create_response(500, 'Error in registering user.')
        return response
    
    response = create_response(200, 'Email {} registered!'.format(email))
    return response


def create_response(statusCode, body):
    response = {
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }
    response['statusCode'] = statusCode
    response['body'] = body
    print('Response: %s' % (response))
    return response