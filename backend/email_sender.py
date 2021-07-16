import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = "dropbox.mailman@gmail.com"
PASSWORD = os.environ['password']  # Password for email account

html = """\
<div dir="ltr">
    <div>
        <div style="text-align:center">
            <font size="4">
                Get started by forwarding this email to:
            </font>
            <br>
        </div>
        <div style="text-align:center">
            <b>
                <font size="4">
                    <a href="mailto:dropbox.mailman@gmail.com" target="_blank">
                        dropbox.mailman@gmail.com
                    </a>
                </font>
            </b>
        </div>
        <br>
        <div style="text-align:center">
            - - - - - - -
        </div>
        <div style="text-align:center">
            <b>
                <font size="4">
                    Shortcut to productivity
                </font>
            </b>
        </div>
        <div style="text-align:center">
            Capture important emails and their files within the Mailman folder on your Dropbox
        </div>
        <br>
        <div style="text-align:center">
            <b>
                <font size="4">
                    Direct files to the right place
                </font>
            </b>
        </div>
        <div style="text-align:center">
            Designate where to save individual emails by including the folder path in the email body
        </div>
    </div>
    <br>
    <br>
    <div style="text-align:center">
            <font color="#999999">
                Yey! 
                <a href="https://app.dropboxer.net/hackdash/2021/projects/4214">
                    <font color="#999999">
                        Hack Week 2021
                    </font>
                </a>
            </font>
    </div>
</div>
"""
body = MIMEText(html, "html")

def send_confirmation_email(recipient):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Get started with Dropbox Mailman 📫"
    message["From"] = EMAIL
    message["To"] = recipient
    message.attach(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(
            EMAIL, recipient, message.as_string()
        )