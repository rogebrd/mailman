from datetime import datetime
import imaplib
import os


USERNAME = os.environ['username']  # Username for email account
PASSWORD = os.environ['password']  # Password for email account

IMAP_GMAIL_SERVER = "imap.gmail.com"


class EmailFetcher:
  def clean_foldername(self, text):
    """Cleans text for creating a folder."""
    return "".join(c if c.isalnum() else "_" for c in text)

  def fetch_account_emails(self, username, password):
    """Fetches all emails given username and password of account"""
    # create imap subclass that connects over SSL encrypted pocket
    imap = imaplib.IMAP4_SSL(IMAP_GMAIL_SERVER)
    imap.login(username, password)
    status, messages = imap.select()
    message_count = int(messages[0])
    return message_count

def lambda_handler(event, context):
    print('Fetching emails for {} at {}...'.format(USERNAME, event['time']))
    num_emails = 0
    try:
      fetcher = EmailFetcher()
      num_emails = fetcher.fetch_account_emails(USERNAME, PASSWORD)
    except:
        print('Fetch failed!')
        raise
    else:
        print('Fetch succeeded! {} emails found'.format(num_emails))
    finally:
        print('Fetch completed at {}'.format(str(datetime.now())))
