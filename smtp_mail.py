#!/usr/bin/env python

import smtplib
from os.path import basename
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication

# Mail Config
sender = #Sender Email ID
receiver = #Receiver Email ID
username = #Sender Email ID
password = #Password
server = smtplib.SMTP('smtp.gmail.com:587') # SMTP established with gmail
server.starttls()  #Enc Type
server.login(username, password)

# Message Config
msg = MIMEMultipart('alternative')
msg['Subject'] = "Status"
msg['From'] = sender
msg['To'] = receiver
msg['preamble'] = 'This is a multi-part message in MIME format.'
file = 'path/to/file'
text = "Hello There!"
msg.attach(MIMEText(text))

# Read File and attach
with open(file, "rb") as fil:
    part = MIMEApplication(
        fil.read(),
        Name=basename(file)
    )
part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
msg.attach(part)


server.sendmail(sender, receiver, msg.as_string())
server.quit()
