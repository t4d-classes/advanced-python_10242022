# Run a local SMTP Server for debugging - does not support SSL
# python -m smtpd -c DebuggingServer -n localhost:1025

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# set some email parameters
host = "localhost"
port = 1025
password = "somepass"

sender_email = "sender@fakedomain.com"
receiver_email = "receiver@fakedomain.com"
subject = "test message"

body = "This message is sent from Python."

# build a multi-part email to support HTML/text as well as attachments
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain", "utf-8"))

filename = "test.txt"  # In same directory as script

# Open file attachment in binary mode
with open(filename, "rb") as attachment:
    
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

with smtplib.SMTP(host, port) as server:
    server.sendmail(sender_email, receiver_email, text)

# this code would be used with an email server that supports SSL
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(host, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, text)
