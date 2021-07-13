def lambda_handler(event, context):
    response = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': ""
        }

    print('Response: %s' % (response))
    return response
