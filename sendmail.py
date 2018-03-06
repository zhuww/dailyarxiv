#! /usr/bin/python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import commands

# me == sender's email address
# you == recipient's email address
me = "me@email.com"
you = "you@email.com"

# Create message container - the correct MIME type is multipart/alternative.
date = commands.getoutput('date +%D')
subject ='New issues on archive ' + date 
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
# Change zhuww to your own username 
text = open('mailbody.zhuww','r').read()
html = open('mailhtml.zhuww','r').read()

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()

