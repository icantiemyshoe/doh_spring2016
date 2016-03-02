#example imported from https://docs.python.org/2/library/email-examples.html

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# This will allow the individuals to be put on the same array and then sent throught smtp once    
# to = ["person1@example.com", "person2@example.com", "person3@example.com"]
# msg['To'] = ",".join(to)
# s.sendmail(me, to, msg.as_string())    

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()



