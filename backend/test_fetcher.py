from fetch_email import EmailFetcher
from formatted_email import FormattedEmail 

fetcher = EmailFetcher()
emails = fetcher.fetch_account_emails("dropbox.mailman@gmail.com", "V6siPUCixAn8BshcwTUD", False)
# create wrapper object with formatted attributes
formatted = FormattedEmail(emails[-1])
print(formatted.formatted_subject)
print(formatted.formatted_text)
print(formatted.foldername)
# original imap_tools object is stored as attribute: msg
print(len(formatted.msg.attachments))