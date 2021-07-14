from datetime import datetime
from fetch_email import EmailFetcher
import boto3
import os

EMAIL = 'dropbox.mailman@gmail.com'
PASSWORD = os.environ['password']  # Password for email account

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    print('Fetching emails for {} at {}...'.format(EMAIL, event['time']))
    num_emails = 0
    try:
        fetcher = EmailFetcher()
        emails = fetcher.fetch_account_emails(EMAIL, PASSWORD)
        num_emails = len(emails)

        for email in emails:
            sender = email.from_
            response = dynamodb.get_item(
                TableName='Registrations',
                Key={'email': {'S': sender}},
            )
            item = response['Item']
            oauth_token = item['dropbox_oauth_token']['S']
            # TODO: Use oauth_token to make Dropbox files_upload request
    except:
        print('Fetch failed!')
        raise
    else:
        print('Fetch succeeded! {} emails found'.format(num_emails))
    finally:
        print('Fetch completed at {}'.format(str(datetime.now())))
