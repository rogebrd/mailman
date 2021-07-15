from datetime import datetime
from dropbox_client import MailmanDropboxClient
from fetch_email import EmailFetcher
import boto3
import os

EMAIL = 'dropbox.mailman@gmail.com'
PASSWORD = os.environ['password']  # Password for email account

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    print('Requesting emails for {} at {}...'.format(EMAIL, event['time']))
    num_emails = 0
    try:
        dropbox_client = MailmanDropboxClient()
        fetcher = EmailFetcher()
        emails = fetcher.fetch_account_emails(EMAIL, PASSWORD)
        num_emails = len(emails)

        for email in emails:
            sender = email.from_
            print('Processing email from {}...'.format(sender))
            response = dynamodb.get_item(
                TableName='Registrations',
                Key={'email': {'S': sender}},
            )
            item = response['Item']
            oauth_token = item['dropbox_oauth_token']['S']
            dropbox_client.upload_file_to_dropbox(email.text, '/Mailman', email.subject + '.txt', oauth_token)
            print('Email from {} successfully uploaded to Dropbox!'.format(sender))
    except:
        print('Request failed!')
        raise
    else:
        print('Request succeeded! {} emails found'.format(num_emails))
    finally:
        print('Request completed at {}'.format(str(datetime.now())))
