from imap_tools import MailBox, AND
import config

IMAP_GMAIL_SERVER = "imap.gmail.com"

class EmailFetcher:

  def fetch_account_emails(self, username, password, only_unread=True):
    """
    Fetches all emails given username and password of account.
    Parameters:
      only_unread should only be set to false for testing purposes as it will read
      all emails. Default is reading only unread emails.
    """
    emails = []
    with MailBox(IMAP_GMAIL_SERVER).login(username, password, 'INBOX') as mailbox:
      if only_unread:
        for msg in mailbox.fetch(AND(seen=False)):
          emails.append(msg)
      else:
        for msg in mailbox.fetch():
          emails.append(msg)
    return emails
