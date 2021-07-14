from datetime import datetime
from fetch_email import EmailFetcher
import os

EMAIL = 'dropbox.mailman@gmail.com'
PASSWORD = os.environ['password']  # Password for email account


def lambda_handler(event, context):
    print('Fetching emails for {} at {}...'.format(EMAIL, event['time']))
    num_emails = 0
    try:
      fetcher = EmailFetcher()
      num_emails = len(fetcher.fetch_account_emails(EMAIL, PASSWORD))
    except:
        print('Fetch failed!')
        raise
    else:
        print('Fetch succeeded! {} emails found'.format(num_emails))
    finally:
        print('Fetch completed at {}'.format(str(datetime.now())))
