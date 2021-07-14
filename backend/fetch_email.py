from imap_tools import MailBox, AND
import config

IMAP_GMAIL_SERVER = "imap.gmail.com"


class EmailFetcher:
  def fetch_account_emails(self, username, password):
    """Fetches all emails given username and password of account"""
    unread = []
    with MailBox(IMAP_GMAIL_SERVER).login(username, password, 'INBOX') as mailbox:
      for msg in mailbox.fetch(AND(seen=False)):
        unread.append(msg)
    return unread

if __name__ == "__main__":
  fetcher = EmailFetcher()
  fetcher.fetch_account_emails(config.username, config.password)
