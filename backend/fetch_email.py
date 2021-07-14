from email.header import decode_header
import config
import email
import imaplib


IMAP_GMAIL_SERVER = "imap.gmail.com"


class EmailFetcher:
  def clean_foldername(self, text):
    """Cleans text for creating a folder."""
    return "".join(c if c.isalnum() else "_" for c in text)

  def fetch_account_emails(self, username, password):
    """Fetches all emails given username and password of account"""
    # create imap subclass that connects over SSL encrypted pocket
    imap = imaplib.IMAP4_SSL(IMAP_GMAIL_SERVER)
    imap.login(config.username, config.password)
    status, messages = imap.select()
    message_count = int(messages[0])
    results = []
    for i in range(message_count, 0, -1):
      results.append(self.fetch_email(imap, i))
    return results

  def fetch_email(self, imap, index):
    """Fetches a single email given imap and index of email"""
    messages = imap.fetch(str(index), "(RFC822)")[1]
    result_text = []
    self.fetched_dict = {} # dictionary to return
    for response in messages:
      if isinstance(response, tuple):
        msg = email.message_from_bytes(response[1])
        subject, encoding = decode_header(msg["Subject"])[0]
        date = msg["Date"]

        if isinstance(subject, bytes):
          subject = subject.decode(encoding)
        sender, encoding = decode_header(msg.get("From"))[0]
        if isinstance(sender, bytes):
          sender = sender.decode(encoding)

        result_text.append(f"Subject: {subject}\n")
        result_text.append(f"Sender: {sender}\n")
        result_text.append(f"Date: {date}\n")
        
        if msg.is_multipart():
          self.handle_multipart_message(msg, result_text)
        else:
          self.handle_singlepart_message(msg, result_text)

    self.fetched_dict["date"] = date
    self.fetched_dict["sender"] = sender
    self.fetched_dict["plain"] = ''.join(result_text)
    self.fetched_dict["subject"] = subject

    return self.fetched_dict

  def handle_multipart_message(self, message, result_text):
    """Handles a message that is multipart"""
    attachments = []
    for part in message.walk():
      content_type = part.get_content_type()
      disposition = str(part.get("Content-Disposition"))
      payload = part.get_payload(decode=True)
      if not payload:
        continue

      if content_type == "text/plain" and "attachment" not in disposition:
        body = payload.decode()
        result_text.append(body)
      if content_type == "text/html":
        body = payload.decode()
        self.fetched_dict["html"] = body
      if "attachment" in disposition:
        # download attachment
        attachments.append(payload)
    self.fetched_dict["attachment"] = attachments
  
  def handle_singlepart_message(self, message, result_text):
    """Handles a message that is not multipart"""
    body = message.get_payload(decode=True).decode()
    html_text = ""
    content_type = message.get_content_type()
    if content_type == "text/plain":
      result_text.append(body)
    elif content_type == "text/html":
      self.fetched_dict["html"] = body

if __name__ == "__main__":
  fetcher = EmailFetcher()
  fetcher.fetch_account_emails(config.username, config.password)
